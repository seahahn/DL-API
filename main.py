from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db_api import schemas
from typing import List

app = FastAPI()

origins = [
    "http://localhost:3000", # 포트 지정 안 하면 CORS 에러 발생
    "https://front-web-xi.vercel.app"
]

origin_regex = "https://.*\.aiplay\.online"

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_origin_regex=origin_regex,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from db_api.api import (
    index, create_post, update_post, delete_post, read_posts, read_posts_by_div, read_post
)

index = app.get("/")(index)
create_post = app.post("/posts/", response_model=schemas.AiPost)(create_post)
update_post = app.put("/posts/{post_id}", response_model=schemas.AiPost)(update_post)
delete_post = app.delete("/posts/{post_id}")(delete_post)
read_posts = app.get("/posts/", response_model=List[schemas.AiPost])(read_posts)
read_posts_by_div = app.get("/posts/{div}", response_model=List[schemas.AiPost])(read_posts_by_div)
read_post = app.get("/posts/{post_id}", response_model=schemas.AiPost)(read_post)


from StarGAN import (
    hair_color_gen
)

hair_color_gen = app.post("/cv/hair_color_gen")(hair_color_gen)