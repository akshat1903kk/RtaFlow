from fastapi import APIRouter, Depends, HTTPException

from .. import models, schemas
from ..database import db_dependency, get_db
from ..utils.auth_utils import create_access_token, hash_password, verify_password
from ..utils.depndencies import require_admin

router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Auth"],
)


# =====================================================
# REGISTER USER
# =====================================================
@router.post("/register", response_model=schemas.UserResponse, status_code=201)
def register_user(model: schemas.UserCreate, db=Depends(get_db)):
    user_exists = (
        db.query(models.User).filter(models.User.username == model.username).first()
    )
    if user_exists:
        raise HTTPException(status_code=400, detail="Username already taken")

    hashed_pw = hash_password(model.password)

    user_count = db.query(models.User).count()

    new_user = models.User(
        username=model.username,
        email=model.email,
        password_hash=hashed_pw,
        role="admin" if user_count == 0 else "user",
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


# =====================================================
# LOGIN USER
# =====================================================
@router.post("/login")
def login_user(model: schemas.UserLogin, db=Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == model.username).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    if not verify_password(model.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    access_token = create_access_token({"sub": user.username, "id": user.id})

    return {"access_token": access_token, "token_type": "bearer"}


# =====================================================
# Protected route helpers
# =====================================================


@router.patch("/role/{user_id}", dependencies=[Depends(require_admin)])
def RoleUpdate(user_id: int, payload: schemas.RoleUpdate, db: db_dependency):
    new_role = payload.new_role.lower()

    allowed_roles = {"admin", "user", "non-admin"}

    if new_role not in allowed_roles:
        raise HTTPException(status_code=400, detail="invalid role")

    user = db.query(models.User).filter(models.User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.role = new_role  # type: ignore
    db.commit()
    db.refresh(user)

    return user
