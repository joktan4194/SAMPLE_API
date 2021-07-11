from sqlalchemy import Column, Integer, String

from .db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, index=True)
    # created_date=Column(String, default=func.now(), nullable=False)
