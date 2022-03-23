import datetime
from pydantic import BaseModel


class AiPostBase(BaseModel):
    div: str
    image_src: str
    author: str
    category: str
    title: str
    dsc: str
    link: str

class AiPostCreate(AiPostBase):
    pass

class AiPost(AiPostBase):
    idx: int
    created_at: datetime.datetime

    class Config:
        orm_mode = True
