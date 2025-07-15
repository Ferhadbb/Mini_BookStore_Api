from fastapi import FastAPI
from app.core.database import engine
from app.models import Base
from app.routers import users, books, orders

# This line creates the database tables(checks if it already exists)

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Mini BookStore ",
    version="0.1.0",
)

# routers
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(books.router, prefix="/books", tags=["books"])
app.include_router(orders.router, prefix="/orders", tags=["orders"])

@app.get("/")
def read_root():

    return {"message": "Welcome to the Mini BookStore API!"} 