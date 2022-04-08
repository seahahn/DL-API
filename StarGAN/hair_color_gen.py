from StarGAN.processor import processing
from fastapi import UploadFile
from fastapi.responses import StreamingResponse

MIME_IMG = ["image/jpg", "image/jpeg", "image/png"]

async def hair_color_gen(img: UploadFile):
    """
    인물 이미지 넣으면 머리색 바꿔주는 딥 러닝 모델 API

    Args:
        img (UploadFile): 입력된 인물 이미지 파일

    Returns:
        blob: 변환된 인물 이미지 파일
    """
    if img.content_type in MIME_IMG:
        processed_img = processing(img)
    else:
        return False

    await img.close()

    return StreamingResponse(processed_img, media_type="image/png")