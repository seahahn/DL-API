from fastapi import UploadFile
from processor import processing

MIME_IMG = "image/*"

async def hair_color_gen(file: UploadFile):
    if file.content_type == MIME_IMG:
        img = await file.read()
    else:
        return False

    processed_img = processing(img)
    await file.close()

    return processed_img