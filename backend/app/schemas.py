from datetime import datetime

from pydantic import BaseModel, Field

# =====================================================
#  Auth schemas
# =====================================================


class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    role: str
    created_at: datetime

    class Config:
        from_attributes = True


# =====================================================
#  TASK SCHEMAS
# =====================================================


class TaskBase(BaseModel):
    title: str = Field(..., max_length=255)
    description: str | None = None
    completed: bool = False


class TaskCreate(TaskBase):
    """Used for creating new tasks."""

    pass


class TaskUpdate(BaseModel):
    """Used for partial updates."""

    title: str | None = Field(None, max_length=255)
    description: str | None = None
    completed: bool | None = None


class Task(TaskBase):
    """Response model for task objects."""

    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True  # Enables ORM → Pydantic conversion


# =====================================================
#  JOURNAL SCHEMAS
# =====================================================


class JournalBase(BaseModel):
    title: str = Field(..., max_length=255)
    content: str | None = None


class JournalCreate(JournalBase):
    """Used for creating journal entries."""

    pass


class JournalUpdate(BaseModel):
    """Used for partial journal updates."""

    title: str | None = Field(None, max_length=255)
    content: str | None = None


class JournalEntry(JournalBase):
    """Response model for journal entries."""

    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
