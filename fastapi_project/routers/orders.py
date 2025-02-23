from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import OrderSchema
from database import SessionLocal, OrderDB, UserDB
from typing import List

router = APIRouter(prefix="/orders", tags=["Orders"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/{user_id}/create")
def create_order(user_id: int, order: OrderSchema, db: Session = Depends(get_db)):
    user = db.query(UserDB).filter(UserDB.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    new_order = OrderDB(item=order.item, quantity=order.quantity, user_id=user.id)
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order
