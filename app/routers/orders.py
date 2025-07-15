from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas import order as order_schema
from app.services import order_service
from app.core.database import get_db
from app.routers.deps import get_current_user
from app.models.user import User

router = APIRouter()

@router.post("/", response_model=order_schema.Order)
def create_order(
    order: order_schema.OrderCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return order_service.create_order(db=db, order=order, user=current_user)

@router.get("/", response_model=List[order_schema.Order])
def read_orders(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return order_service.get_user_orders(db=db, user=current_user) 