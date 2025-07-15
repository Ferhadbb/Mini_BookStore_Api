from sqlalchemy import Column, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.core.database import Base


order_book_association = Table(
    "order_book",
    Base.metadata,
    Column("order_id", Integer, ForeignKey("orders.id")),
    Column("book_id", Integer, ForeignKey("books.id")),
)

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="orders")
    books = relationship("Book", secondary=order_book_association) 