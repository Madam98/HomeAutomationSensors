from fastapi import Depends, status, APIRouter
from ..sql_app import models, schemas
from sqlalchemy.orm import Session
from ..hashing import Hash
from ..dependencies import get_db
from typing import List


router = APIRouter(
    prefix="/users",
    tags=["users"],
    # dependencies=[Depends(get_token_header)],    # wymóg autoryzacji dla wszystkich endpointów w tym module
    responses={
        404: {
            "description": "Not found"
        }
    })


# create a new user account
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = models.User(email=request.email, hashed_password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"New added user": new_user}


# delete a user account
@router.delete("/{user_id}")
def destroy(user_id: int, db: Session = Depends(get_db), status_code=200):
    db.query(models.User).filter(models.User.id == user_id).delete(synchronize_session=False)
    db.commit()
    return {"message": "User deleted"}


# show all user accounts
@router.get("/", response_model=List[schemas.ShowUser])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.User).offset(skip).limit(limit).all()
