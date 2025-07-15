from pydantic import BaseModel
from typing import Optional

# --- Book Schemas ---

class BookBase(BaseModel):

    title: str
    author: str
    price: float

class BookCreate(BookBase):

    pass

class BookUpdate(BaseModel):

    title: Optional[str] = None
    author: Optional[str] = None
    price: Optional[float] = None

class Book(BookBase):

    id: int
    is_deleted: bool

    class Config:

        from_attributes = True 