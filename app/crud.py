import datetime
from sqlalchemy.orm import Session
from . import models, schemas

def create_address_request_entry(db: Session, address: str):
    db_entry = models.AddressRequestHistory(requested_address=address)

    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)

    return db_entry

def history_entries(db: Session, skip: int=0, limit: int=10):
    return db.query(models.AddressRequestHistory)\
        .order_by(models.AddressRequestHistory.timestamp.desc())\
        .offset(skip).\
        limit(limit).\
        all()

def count_history_entries(db: Session) -> int:
    return db.query(models.AddressRequestHistory).count()