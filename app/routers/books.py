from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas import book as book_schema
from app.services import book_service
from app.core.database import get_db
from app.routers.deps import get_current_user
from app.models.user import User

router = APIRouter()

@router.post("/", response_model=book_schema.Book)
def create_book(
    book: book_schema.BookCreate, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return book_service.create_book(db=db, book=book)

@router.get("/", response_model=List[book_schema.Book])
def read_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):

    books = book_service.get_books(db, skip=skip, limit=limit)
    return books

@router.get("/{book_id}", response_model=book_schema.Book)
def read_book(book_id: int, db: Session = Depends(get_db)):

    db_book = book_service.get_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@router.put("/{book_id}", response_model=book_schema.Book)
def update_book(
    book_id: int, 
    book: book_schema.BookUpdate, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    db_book = book_service.update_book(db, book_id=book_id, book_update=book)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@router.delete("/{book_id}", response_model=book_schema.Book)
def delete_book(
    book_id: int, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    db_book = book_service.delete_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book 