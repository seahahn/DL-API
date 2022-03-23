from StarGAN.processor import processing
from fastapi import UploadFile
from fastapi.responses import StreamingResponse

MIME_IMG = ["image/jpg", "image/jpeg", "image/png"]

async def hair_color_gen(img: UploadFile):
    if img.content_type in MIME_IMG:
        processed_img = processing(img)
    else:
        return False

    await img.close()

    return StreamingResponse(processed_img, media_type="image/png")