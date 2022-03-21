from typing import Optional, List
from fastapi import FastAPI, File, UploadFile
import os

app = FastAPI()


@app.get('/')
def read_root():
    print(1)
    return {"Hello": "World"}


@app.post('/files/')
def files(files: List[bytes]= File(...)):
    # print(files)
    return {"file_sizes": [len(file) for file in files]}


@app.post('/uploadfile')
async def upload_file(files: List[UploadFile] = File(...)):
    upload_directory = 'D:/AIPlay/DL-API/fastapi/files'
    for file in files:
        contents = await file.read()
        with open(os.path.join(upload_directory, file.filename), 'wb') as fp:
            fp.write(contents)
        print(file.filename)
    return {'filename': [file.filename for file in files]}