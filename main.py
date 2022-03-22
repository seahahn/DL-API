from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000" # 포트 지정 안 하면 CORS 에러 발생
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from StarGAN import (
    hair_color_gen
)

hair_color_gen = app.post("/cv/hair_color_gen")(hair_color_gen)