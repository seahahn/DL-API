## Import Lib
import torch
from torch.utils import data
import torchvision.transforms as T
from PIL import Image
import os
# import torchvision
# from torchvision.datasets import ImageFolder
# import matplotlib.pyplot as plt

## CreateDataset
class CreateDataset(data.Dataset):
    # 입력 받은 이미지를 모델이 변환할 수 있도록 바꾸는 클래스
    def __init__(self, image_file, label, transform):  # image_dir, image_name은 바꿔야 하는 사항 / 웹에서 이미지 자체를 가져옴.
        # self.image_dir = image_dir
        # self.image_name = image_name
        self.image_file = image_file
        self.label = label
        self.transform = transform # 이미지의 크기나 정규화, tensor 변환등을 가지고 있음.
        self.dataset = [[self.label]]


    def __getitem__(self, index):
        label = self.dataset[index]
        # image = Image.open(os.path.join(self.image_dir, filename)).convert('RGB')
        image = Image.open(self.image_file).convert('RGB')
        return self.transform(image), torch.FloatTensor(label)


    def __len__(self):
        return len(self.dataset)


def loader(image_file, label, crop_size, image_size):
    transform = T.Compose([
        T.CenterCrop(crop_size),
        T.Resize(image_size),
        T.ToTensor(),
        T.Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5))])  # tanh를 사용하기 때문에 -1 ~ 1로 정규화를 해준다.

    dataset = CreateDataset(image_file, label, transform)
    dataloader = data.DataLoader(
        dataset=dataset,
        batch_size=1,
        num_workers=0)

    return dataloader


# 여러가지 도메인의 content_attrs를 만들어줌.
def create_domains(c_org, c_dim=5, select_attrs=None):
    hair_color_indices = []
    for i, attr_name in enumerate(select_attrs):
        if attr_name in ['Black_Hair', 'Blond_Hair', 'Brown_Hair', 'Gray_Hair']:
            hair_color_indices.append(i)

    c_trg_list = []
    for i in range(c_dim):
        c_trg = c_org.clone()
        if i in hair_color_indices:  # Set one hair color to 1 and the rest to 0.
            c_trg[:, i] = 1
            for j in hair_color_indices:
                if j != i:
                    c_trg[:, j] = 0
        else:
            c_trg[:, i] = (c_trg[:, i] == 0)  # Reverse attribute value.

        c_trg_list.append(c_trg)
    return c_trg_list