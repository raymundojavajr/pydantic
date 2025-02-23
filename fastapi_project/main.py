from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional

app = FastAPI()

# ✅ Pydantic Model for Validation
class UserSchema(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=128)

users_db = []

# ✅ Route to Create User (Uses Pydantic for Validation)
@app.post("/users/")
def create_user(user: UserSchema):
    users_db.append(user.dict())  # Store valid data
    return {"message": "User created successfully", "user": user}

# ✅ Route to Get All Users
@app.get("/users/", response_model=List[UserSchema])
def get_users():
    return users_db

@app.get("/")
def root():
    return {"message": "FastAPI with Pydantic is working!"}
