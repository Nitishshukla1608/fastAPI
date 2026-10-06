# # from fastapi import FastAPI, Query, Body, HTTPException, status 
# # from pydantic import BaseModel

# # app = FastAPI()

from fastapi import FastAPI



# # # @app.get("/shipment/{id}")
# # # def read_root(id):
# # #     return {
# # #         "id": id,
# # #         "product": "chair",
# # #         "price": 100
# # #     }   // functional path parameter



# # from fastapi import FastAPI

# # app = FastAPI()

# # # @app.get("/shipment")
# # # def get_shipment(id: int):
# # #     return {
# # #         "id": id,
# # #         "product": "chair",
# # #         "price": 100
# # #     } 



# # # @app.get("/shipment")
# # # def get_package(
# # #     weight: int = Query(..., ge=1, le=100)
# # # ):
# # #     return {
# # #         "weight": weight,
# # #         "status": "Package Accepted"
# # #     }




# # shipments = {
# #     1270: {"weight": 12.5, "content": "wooden table", "status": "delivered"},
# #     1271: {"weight": 13.5, "content": "toys", "status": "pending"},
# #     1272: {"weight": 10.2, "content": "chair", "status": "shipped"},
# #     1273: {"weight": 5.1, "content": "books", "status": "pending"},
# #     1274: {"weight": 22.0, "content": "refrigerator", "status": "delivered"},
# #     1275: {"weight": 3.7, "content": "clothes", "status": "shipped"},
# #     1276: {"weight": 8.9, "content": "shoes", "status": "pending"},
# #     1277: {"weight": 15.0, "content": "monitor", "status": "delivered"},
# #     1278: {"weight": 6.3, "content": "keyboard", "status": "shipped"},
# #     1279: {"weight": 1.1, "content": "mouse", "status": "pending"},
# # }


# # @app.get("/shipment")
# # def get_shipment(id: int):
# #     shipment = shipments.get(id)

# #     if shipment is None:
# #         raise HTTPException(
# #             status_code=status.HTTP_404_NOT_FOUND,
# #             detail=f"Shipment with id {id} is not present"
# #         )

# #     return shipment;



# # # post requests
# # @app.post("/new-shipment")
# # def new_shipment(weight: float = Body(...), content: str = Body(...)):
# #     if weight <= 0:
# #         raise HTTPException(
# #             status_code=status.HTTP_406_NOT_ACCEPTABLE,
# #             detail="weight must be greater than 0",
# #         )

# #     new_id = max(shipments) + 1

# #     new_shipments = {
# #         "id": new_id,
# #         "weight": weight,
# #         "content": content,
# #         "status": "Placed",
# #     }

# #     shipments[new_id] = new_shipments

# #     return {"message": f"order placed successfully{new_id}"}



# # @app.put("/update-shipment/{sid}")
# # def update_shipment(sid: int, data: UpdateShipment):

# #     if sid not in shipments:
# #         raise HTTPException(
# #             status_code=status.HTTP_404_NOT_FOUND,
# #             detail="Product with this id is not available"
# #         )

# #     shipments[sid].update({
# #         "weight": data.weight,
# #         "content": data.content,
# #         "status": Status.SHIPPED.value
# #     })

# #     return {
# #         "message": f"Shipment {sid} updated successfully",
# #         "shipment": shipments[sid]
# #     }




# # # update specific part only

# # @app.patch("/update-shipment/{ship_id}")
# # def update_only_one(
# #     ship_id: int,
# #     weight: float | None = Body(None),
# #     content: str | None = Body(None)
# # ):
# #     if ship_id not in shipments:
# #         raise HTTPException(
# #             status_code=status.HTTP_404_NOT_FOUND,
# #             detail="Product with this id is not available",
# #         )

# #     shipments[ship_id].update({
# #         "weight": weight,
# #         "content": content
# #     })

# #     return {
# #         "message": "shipment is updated",
# #         "data": shipments[ship_id]
# #     }



# # @app.delete("/delete-shipment/{ship_id}")
# # def delete_shipment(ship_id: int):
# #     if ship_id not in shipments:
# #         raise HTTPException(
# #             status_code=status.HTTP_404_NOT_FOUND,
# #             detail="Product with this id is not available"
# #         )

# #     shipments.pop(ship_id)

# #     return {
# #         "message": f"Shipment {ship_id} deleted successfully"
# #     }



   
# from fastapi import FastAPI, Depends
# from sqlalchemy.ext.asyncio import AsyncSession

# from database import get_db, engine, Base
# from models import User

# app = FastAPI()


# @app.on_event("startup")
# async def startup():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)


# @app.post("/users")
# async def create_user(db: AsyncSession = Depends(get_db)):

#     user = User(
#         name="John",
#         email="john@example.com"
#     )

#     db.add(user)

#     await db.commit()
#     await db.refresh(user)

#     return user




from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import User
from schemas import UserCreate, UserResponse
from hash import generate_password

router = APIRouter(prefix="/users", tags=["Users"])

app = FastAPI() 

@router.post("/", response_model=UserResponse)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    hashed_password = hash_password(user.password)

    new_user = User(
        username=user.username,
        email=user.email,
        password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

