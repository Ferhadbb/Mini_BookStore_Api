from pydantic import BaseModel
from typing import List
from .book import Book

# --- Order Schemas ---

class OrderCreate(BaseModel):

    book_ids: List[int]

class Order(BaseModel):

    id: int
    user_id: int
    books: List[Book] = []

    class Config:
        from_attributes = True 