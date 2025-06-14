from typing import List, Optional
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select

from ..database import get_session
from ..models.order import Order, OrderCreate, OrderRead, OrderUpdate

router = APIRouter()

@router.post("/orders/", response_model=OrderRead)
def create_order(
    order: OrderCreate,
    session: Session = Depends(get_session),
):
    db_order = Order.from_orm(order)
    session.add(db_order)
    session.commit()
    session.refresh(db_order)
    return db_order

@router.get("/orders/", response_model=List[OrderRead])
def read_orders(
    skip: int = 0,
    limit: int = 100,
    order_status: Optional[str] = Query(None, description="Filter by order status"),
    #customer_id: Optional[int] = Query(None, description="Filter by customer ID"),
    #quote_id: Optional[int] = Query(None, description="Filter by quote ID"),
    session: Session = Depends(get_session),
):
    query = select(Order)

    if order_status:
        query = query.where(Order.order_status == order_status)
    #if customer_id is not None:
        #query = query.where(Order.customer_id == customer_id)
    #if quote_id is not None:
        #query = query.where(Order.quote_id == quote_id)

    orders = session.exec(query.offset(skip).limit(limit)).all()
    return orders

@router.get("/orders/{order_id}", response_model=OrderRead)
def read_order(
    order_id: int,
    session: Session = Depends(get_session),
):
    order = session.get(Order, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.patch("/orders/{order_id}", response_model=OrderRead)
def update_order(
    order_id: int,
    order_update: OrderUpdate,
    session: Session = Depends(get_session),
):
    db_order = session.get(Order, order_id)
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")

    order_data = order_update.dict(exclude_unset=True)
    for key, value in order_data.items():
        setattr(db_order, key, value)

    db_order.updated_at = datetime.utcnow()
    session.add(db_order)
    session.commit()
    session.refresh(db_order)
    return db_order

@router.delete("/orders/{order_id}")
def delete_order(
    order_id: int,
    session: Session = Depends(get_session),
):
    order = session.get(Order, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    session.delete(order)
    session.commit()
    return {"ok": True, "message": "Order deleted successfully"}