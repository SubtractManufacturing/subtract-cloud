from typing import Optional
from datetime import datetime, timezone
from sqlmodel import Field, SQLModel, Relationship
from pydantic import validator

# Base model with common fields
class OrderBase(SQLModel):
    #customer_id: int = Field(foreign_key="customer.id", index=True)
    #quote_id: int = Field(foreign_key="quote.id", index=True)
    order_status: str = Field(default="pending")
    total_price: float

    @validator("order_status")
    def validate_order_status(cls, v):
        allowed = ["pending", "confirmed", "processing", "shipped", "delivered", "cancelled"]
        if v not in allowed:
            raise ValueError(f"order_status must be one of {allowed}")
        return v

# Table model
class Order(OrderBase, table=True):
    order_id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=datetime.now(timezone.utc))

    # relationships (assuming you have Customer and Quote models defined elsewhere)
    #customer: Optional["Customer"] = Relationship(back_populates="orders")
    #quote: Optional["Quote"] = Relationship(back_populates="orders")

# API models
class OrderCreate(OrderBase):
    """
    Fields required to create an order.
    order_id, created_at, updated_at will be generated.
    """

class OrderRead(OrderBase):
    order_id: int
    created_at: datetime
    updated_at: datetime

class OrderUpdate(SQLModel):
    #customer_id: Optional[int] = Field(default=None, foreign_key="customer.id")
    #quote_id: Optional[int] = Field(default=None, foreign_key="quote.id")
    order_status: Optional[str] = None
    total_price: Optional[float] = None