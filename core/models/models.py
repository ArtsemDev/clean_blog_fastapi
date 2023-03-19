from datetime import datetime

from sqlalchemy import Column, VARCHAR, TEXT, TIMESTAMP

from .base import Base


class Post(Base):
    title = Column(VARCHAR(128), nullable=False, unique=True)
    body = Column(TEXT, nullable=False)
    date_created = Column(TIMESTAMP, default=datetime.now())
    slug = Column(VARCHAR(128), nullable=False, unique=True)
