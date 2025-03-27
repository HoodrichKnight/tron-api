import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from .database import Base

class AddressRequestHistory(Base):
    __tablename__ = "address_request_history"

    id = Column(Integer, primary_key=True, index=True)
    requested_address = Column(String, index=True, nullable=False)

    timestamp = Column(DateTime(timezone=True), server_default=func.now())
