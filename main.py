from fastapi import FastAPI
from models import User,Gender,Role
from typing import List
from uuid import uuid4,UUID

app = FastAPI()

db:List[User] = [
            User(
                id=uuid4(), 
                first_name="Jamila",
                last_name="Ahmed",
                middle_name="",
                gender=Gender.female,
                roles=[Role.student]),
            User(
                id=uuid4(), 
                first_name="Alex",
                last_name="Jones",
                middle_name="",
                gender=Gender.male,
                roles=[Role.admin, Role.user])

]
@app.get("/")
async def root():
    return {"Hello": "test"}
@app.get("/api/test")
async def fetch_users():
    return db
@app.post("/api/v1/test")
async def register(user: User):
    db.append(user)
    return {"id": user.id }
@app.delete("/api/v1/test/{user_id}")
async def delete(user_id: UUID): 
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return 

