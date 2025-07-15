from sqlalchemy import Column, Integer, String, Float, Boolean
from app.core.database import Base

class Book(Base):

    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    author = Column(String, index=True, nullable=False)
    price = Column(Float, nullable=False)
    is_deleted = Column(Boolean, default=False) 