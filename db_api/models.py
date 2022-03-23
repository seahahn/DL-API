from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from db_api.database import Base


class AiPost(Base):
    __tablename__ = "ai_example"

    idx = Column(Integer, primary_key=True, index=True)
    div = Column(String)
    image_src = Column(String)
    author = Column(String)
    category = Column(String)
    title = Column(String)
    dsc = Column(String)
    link = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())