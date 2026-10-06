from fastapi import FastAPI
from contextlib import contextmanager
from sqlmodel import SQLModel
from database.models import Shipment , ShipmentStatus
from schemas import Ship,ShipmentStaus

@contextmanager
async def lifespan(app:FastAPI):