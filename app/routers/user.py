from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, schemas
from app.dependencies import get_db

router = APIRouter()

# 👉 CREATE USER
@router.post("/user", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = models.UserModel(name=user.name, age=user.age)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# 👉 GET USERS
@router.get("/user")
def get_users(db: Session = Depends(get_db)):
    return db.query(models.UserModel).all()