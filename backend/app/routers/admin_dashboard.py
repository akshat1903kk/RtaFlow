from typing import List

from fastapi import APIRouter, Depends, HTTPException

from ..database import db_dependency
from ..models import User
from ..schemas import UserResponse, UserUpdate
from ..utils.auth_utils import hash_password
from ..utils.depndencies import require_admin

router = APIRouter(prefix="/api/v1/admin/dashboard", tags=["admin-dashboard"])


@router.get(
    "/users",
    response_model=List[UserResponse],
    dependencies=[Depends(require_admin)],
)
def fetch_all_user(db: db_dependency):
    users = db.query(User).all()
    if not users:
        raise HTTPException(status_code=404, detail="No users found")
    return users


@router.get(
    "/users/{user_id}",
    response_model=UserResponse,
    dependencies=[Depends(require_admin)],
)
def fetch_single_user(user_id: int, db: db_dependency):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.patch(
    "/users/{user_id}",
    response_model=UserResponse,
    dependencies=[Depends(require_admin)],
)
def patch_user(user_id: int, update: UserUpdate, db: db_dependency):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Handle role change
    if update.role:
        if update.role not in ["admin", "user"]:
            raise HTTPException(status_code=400, detail="Invalid role")

        # prevent demoting the only admin
        if user.role == "admin" and update.role == "user":
            total_admins = db.query(User).filter(User.role == "admin").count()
            if total_admins <= 1:
                raise HTTPException(
                    status_code=400,
                    detail="Cannot demote the only admin in the system",
                )

        user.role = update.role

    # Handle password reset
    if update.password:
        user.password_hash = hash_password(update.password)

    db.commit()
    db.refresh(user)
    return user


@router.delete(
    "/users/{user_id}",
    dependencies=[Depends(require_admin)],
)
def delete_user(user_id: int, db: db_dependency):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Block deleting the only admin
    if user.role == "admin":
        total_admins = db.query(User).filter(User.role == "admin").count()
        if total_admins <= 1:
            raise HTTPException(
                status_code=400,
                detail="Cannot delete the only admin in the system",
            )

    db.delete(user)
    db.commit()

    return {"detail": f"User with id {user_id} deleted successfully"}
