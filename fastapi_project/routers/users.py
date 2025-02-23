from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import UserSchema, UserResponse
from database import SessionLocal, UserDB
from auth import hash_password, create_access_token, verify_password

router = APIRouter(prefix="/users", tags=["Users"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=UserResponse)
def create_user(user: UserSchema, db: Session = Depends(get_db)):
    existing_user = db.query(UserDB).filter(UserDB.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_pw = hash_password(user.password)
    new_user = UserDB(name=user.name, email=user.email, password=hashed_pw)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/login")
def login_user(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(UserDB).filter(UserDB.email == email).first()
    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    token = create_access_token(data={"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}
