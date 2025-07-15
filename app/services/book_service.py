from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.book import Book
from app.schemas.book import BookCreate, BookUpdate

def get_book(db: Session, book_id: int) -> Optional[Book]:

    return db.query(Book).filter(Book.id == book_id, Book.is_deleted == False).first()

def get_books(db: Session, skip: int = 0, limit: int = 10) -> List[Book]:

    return db.query(Book).filter(Book.is_deleted == False).offset(skip).limit(limit).all()

def create_book(db: Session, book: BookCreate) -> Book:

    db_book = Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def update_book(db: Session, book_id: int, book_update: BookUpdate) -> Optional[Book]:

    db_book = get_book(db, book_id)
    if db_book:
        for key, value in book_update.dict(exclude_unset=True).items():
            setattr(db_book, key, value)
        db.commit()
        db.refresh(db_book)
    return db_book

def delete_book(db: Session, book_id: int) -> Optional[Book]:
    db_book = get_book(db, book_id)
    if db_book:
        db_book.is_deleted = True
        db.commit()
        db.refresh(db_book)
    return db_book 