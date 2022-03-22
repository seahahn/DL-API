from .processor import processing
from fastapi import UploadFile
from fastapi.responses import StreamingResponse

MIME_IMG = ["image/jpg", "image/jpeg", "image/png", "image/gif", "image/bmp"]

async def hair_color_gen(img: UploadFile):
    print(img.content_type)
    if img.content_type in MIME_IMG:
        print("file in")
        # img = await img.read()
        processed_img = processing(img)
    else:
        print("file not img")
        return False

    print("processed")
    await img.close()
    print("closed")
    
    return StreamingResponse(processed_img, media_type="image/png")