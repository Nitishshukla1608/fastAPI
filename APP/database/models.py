from asyncio import CancelledError
from enum import Enum
from logging import PlaceHolder
from multiprocessing.connection import deliver_challenge
from turtle import window_height
from APP.database import shipment_status
from sqlmodel import SQLModel


class ShipmentStatus(str , Enum):
    placed = "placed"
    delivered = "delivered"
    in_transit = "in_transit"
    cancelled = "cancelled"
    CancelledErrorpending = "pending"
    shipped = "shipped"






class Shipment(SQLModel, table=True):
    __tablename__ = "shipments"
    id:int|None = Field(default = None , primary_key = True)
    content:str
    weight:float = Field(ge = 0, le = 20)
    status : ShipmentStatus = Field(default = ShipmentStatus.placed)
    destination:str
    expected_delivery:datatime