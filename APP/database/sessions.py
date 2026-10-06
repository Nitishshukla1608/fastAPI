from sqlalchemy import create_engine
from sqlmodel import SQLModel
from database.models import Shipment , ShipmentStatus

engine = create_engine(url = "sqlite:///shipment.db",echo = True, connect_args = {"check_same_thread":False})

def create_db_and_tabnle():
    SQLModel.metadata.create_all(bind = engine)
