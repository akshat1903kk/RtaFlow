from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from .. import models, schemas
from ..config import settings
from ..database import get_db
from ..utils.auth_utils import create_access_token, hash_password, verify_password

router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Auth"],
)

# OAuth2 scheme for extracting Bearer token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


# =====================================================
# REGISTER USER
# =====================================================
@router.post("/register", response_model=schemas.User, status_code=201)
def register_user(model: schemas.UserCreate, db=Depends(get_db)):
    user_exists = (
        db.query(models.User).filter(models.User.username == model.username).first()
    )
    if user_exists:
        raise HTTPException(status_code=400, detail="Username already taken")

    hashed_pw = hash_password(model.password)

    new_user = models.User(
        username=model.username,
        email=model.email,
        password_hash=hashed_pw,
        role="non-Admin",
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
# GET CURRENT USER (Protected route helper)
# =====================================================
def get_current_user(token: str = Depends(oauth2_scheme), db=Depends(get_db)):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        username = payload.get("sub")
        user_id = payload.get("id")

        if username is None or user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user
