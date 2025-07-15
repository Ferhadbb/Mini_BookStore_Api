from sqlalchemy.orm import Session
from typing import List
from app.models.order import Order
from app.models.book import Book
from app.schemas.order import OrderCreate
from app.models.user import User

def create_order(db: Session, order: OrderCreate, user: User) -> Order:

    db_order = Order(user_id=user.id)
    
    
    books = db.query(Book).filter(Book.id.in_(order.book_ids)).all()
    
  # adds book to cart
    db_order.books.extend(books)
    
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_user_orders(db: Session, user: User) -> List[Order]:

    return db.query(Order).filter(Order.user_id == user.id).all() 