from fastapi import APIRouter, Depends, HTTPException

from backend.app import models

from ..database import db_dependency
from ..utils.depndencies import require_admin

router = APIRouter(prefix="/admin", tags=["admin"])


@router.get("/get_users", dependencies=[Depends(require_admin)])
def get_users(db: db_dependency):
    users = db.query(models.User).all()
    if not users:
        raise HTTPException(status_code=404, detail="no user found")
    return users


@router.get("/fetch_user/{user_id}", dependencies=[Depends(require_admin)])
def fetch_a_user(db: db_dependency, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"no user for user-id : {user_id}")
    return user


@router.delete("/remove/{user_id}", dependencies=[Depends(require_admin)])
def remove_user(user_id: int, db: db_dependency):
    user = db.query(models.User).filter(models.User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user.role == "admin":
        raise HTTPException(status_code=403, detail="Cannot delete an admin user")

    db.delete(user)
    db.commit()

    return {"detail": f"User {user_id} removed successfully"}
