from turtle import window_height
from pydantic import BaseModel
from typing import Optimal

class Ships(BasemOdel):
    weight:float
    content:str


class Response(BaseModel):
    id:int
    weight:float
    content:str
    status:str


class UpdateShipment(BaseModel):
    weight:float
    content:str