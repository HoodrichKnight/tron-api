import datetime
from pydantic import BaseModel, Field
from typing import Optional

class AddressRequest(BaseModel):
    address: str = Field(..., description="Tron address")

class TronAccountInfo(BaseModel):
    address: str
    balance_trx: float
    bandwidth: dict
    energy: dict

class HistoryEntry(BaseModel):
    id: int
    requested_address: str
    timestamp: datetime.datetime

    class Config:
        orm_mode = True

class BandwidthInfo(BaseModel):
    free_net_used: int
    free_net_limit: int

    net_used: Optional[int] = None
    net_limit: Optional[int] = None

    available_free: int
    available_staked: Optional[int] = None

class EnergyInfo(BaseModel):
    energy_used: Optional[int] = None
    energy_limit: Optional[int] = None

    available: Optional[int] = None

class TronAccountInfo(BaseModel):
    address: str
    balance_trx: float
    bandwidth: BandwidthInfo
    energy: EnergyInfo

