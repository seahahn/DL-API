import torch, torchvision
from io import BytesIO
from StarGAN.image_proprecessing import loader, create_domains
from StarGAN.generator import Generator
from StarGAN.func import denorm

def set_generator():
    Gen = Generator(64, 5)  # Generator 생성
    G_path = 'StarGAN/200000-G.ckpt'  # 200000번 학습한 파라미터를 가져옴.

    ## 사전 학습된 파라미터를 생성한 Generator의 파라미터로 교체하는 과정 ######
    G_pratrained_dict = torch.load(G_path, map_location=lambda storage, loc: storage)
    G_new_pretrained_dict = {}
    G_dict = Gen.state_dict()

    for dic in list(G_dict.keys()):
        if dic.split('.')[-1] == 'num_batches_tracked':
            del G_dict[dic]

    key_list = list(G_dict.keys())
    value_list = list(G_pratrained_dict.values())

    for i in range(len(G_pratrained_dict.items())):
        dict_key = key_list[i]
        dict_value = value_list[i]
        G_new_pretrained_dict.update({dict_key: dict_value})

    G_dict.update(G_new_pretrained_dict)
    # 미리 학습된 파라미터를 적용
    Gen.load_state_dict(G_new_pretrained_dict)

    return Gen

def processing(image_file, label=[True, False, False, False, True], crop_size=178, image_size=128):
    dataset = loader(image_file, label, crop_size, image_size)
    _, org_content = next(iter(dataset))
    select_attrs = ['Black_Hair', 'Blond_Hair', 'Brown_Hair', 'Male', 'Young']

    generator = set_generator()
    with torch.no_grad():  # 모델이 학습을 하지 않도록 설정
        for _, (real_img, org_content) in enumerate(dataset):
            content_target_list = create_domains(org_content, 5, select_attrs=select_attrs)

            # 이미지 변환
            x_fake_list = []
            for content_target in content_target_list:
                x_fake_list.append(generator(real_img, content_target))
            x_fake_list = x_fake_list[:3]

            # 이미지 저장
            image_concat = torch.cat(x_fake_list, dim=3)
            grid = torchvision.utils.make_grid(denorm(image_concat.data.cpu()), nrow=1, padding=0)

    processed_img = BytesIO()
    torchvision.utils.save_image(grid, processed_img, "png")
    processed_img.seek(0)

    return processed_img