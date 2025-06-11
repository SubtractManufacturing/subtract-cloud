from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select
from datetime import datetime

from ..database import get_session
from ..models.shipment import Shipment, ShipmentCreate, ShipmentRead, ShipmentUpdate

router = APIRouter()

@router.post("/shipments/", response_model=ShipmentRead)
def create_shipment(shipment: ShipmentCreate, session: Session = Depends(get_session)):
    db_shipment = Shipment.from_orm(shipment)
    session.add(db_shipment)
    session.commit()
    session.refresh(db_shipment)
    return db_shipment

@router.get("/shipments/", response_model=List[ShipmentRead])
def read_shipments(
    skip: int = 0, 
    limit: int = 100, 
    status: Optional[str] = Query(None, description="Filter by status"),
    carrier: Optional[str] = Query(None, description="Filter by carrier"),
    session: Session = Depends(get_session)
):
    query = select(Shipment)
    
    # Apply filters if provided
    if status:
        query = query.where(Shipment.status == status)
    if carrier:
        query = query.where(Shipment.carrier == carrier)
    
    shipments = session.exec(query.offset(skip).limit(limit)).all()
    return shipments

@router.get("/shipments/{shipment_id}", response_model=ShipmentRead)
def read_shipment(shipment_id: int, session: Session = Depends(get_session)):
    shipment = session.get(Shipment, shipment_id)
    if not shipment:
        raise HTTPException(status_code=404, detail="Shipment not found")
    return shipment

@router.get("/shipments/tracking/{tracking_number}", response_model=ShipmentRead)
def get_shipment_by_tracking(tracking_number: str, session: Session = Depends(get_session)):
    query = select(Shipment).where(Shipment.tracking_number == tracking_number)
    shipment = session.exec(query).first()
    if not shipment:
        raise HTTPException(status_code=404, detail="Shipment not found")
    return shipment

@router.patch("/shipments/{shipment_id}", response_model=ShipmentRead)
def update_shipment(
    shipment_id: int, 
    shipment_update: ShipmentUpdate, 
    session: Session = Depends(get_session)
):
    db_shipment = session.get(Shipment, shipment_id)
    if not db_shipment:
        raise HTTPException(status_code=404, detail="Shipment not found")
    
    # Update the shipment with the provided data
    shipment_data = shipment_update.dict(exclude_unset=True)
    for key, value in shipment_data.items():
        setattr(db_shipment, key, value)
    
    # Update the updated_at timestamp
    db_shipment.updated_at = datetime.utcnow()
    
    session.add(db_shipment)
    session.commit()
    session.refresh(db_shipment)
    return db_shipment

@router.delete("/shipments/{shipment_id}")
def delete_shipment(shipment_id: int, session: Session = Depends(get_session)):
    shipment = session.get(Shipment, shipment_id)
    if not shipment:
        raise HTTPException(status_code=404, detail="Shipment not found")
    
    session.delete(shipment)
    session.commit()
    return {"ok": True, "message": "Shipment deleted successfully"}