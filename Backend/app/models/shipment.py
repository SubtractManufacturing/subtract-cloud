from typing import Optional, List
from datetime import datetime
from sqlmodel import Field, SQLModel, Relationship
from pydantic import validator

# Base model with common fields
class ShipmentBase(SQLModel):
    tracking_number: str = Field(index=True)
    carrier: str
    status: str = Field(default="pending")
    origin_address: str
    destination_address: str
    weight_kg: float
    description: Optional[str] = None
    estimated_delivery: Optional[datetime] = None
    
    @validator('status')
    def validate_status(cls, v):
        allowed_statuses = ["pending", "in_transit", "delivered", "failed", "returned"]
        if v not in allowed_statuses:
            raise ValueError(f"Status must be one of {allowed_statuses}")
        return v

# Database model (table definition)
class Shipment(ShipmentBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    
    # You can add relationships here if needed, for example:
    # items: List["ShipmentItem"] = Relationship(back_populates="shipment")

# API models for creating and reading
class ShipmentCreate(ShipmentBase):
    pass

class ShipmentRead(ShipmentBase):
    id: int
    created_at: datetime
    updated_at: datetime

class ShipmentUpdate(SQLModel):
    tracking_number: Optional[str] = None
    carrier: Optional[str] = None
    status: Optional[str] = None
    origin_address: Optional[str] = None
    destination_address: Optional[str] = None
    weight_kg: Optional[float] = None
    description: Optional[str] = None
    estimated_delivery: Optional[datetime] = None