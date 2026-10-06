from enum import Enum
from pydantic import BaseModel
from fastapi import FastAPI


app = FastAPI()


class Status(str, Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"


class User(BaseModel):
    name: str
    status: Status


@app.get("/")
def home():
    return {"message": "FastAPI is working"}


@app.post("/users")
def create_user(user: User):
    return user
    


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

