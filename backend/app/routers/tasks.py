from fastapi import APIRouter, HTTPException

from .. import models, schemas
from ..database import db_dependency

router = APIRouter(
    prefix="/api/v1/tasks",
    tags=["Tasks"],
)

# =====================================================
# Dependencies
# =====================================================
#
# this has been shifted to database.py
#
# =====================================================
# TASK OPERATIONS
# =====================================================


@router.get("/", response_model=list[schemas.Task])
def get_tasks(db: db_dependency):
    """Fetch all tasks."""
    data = db.query(models.Task).all()
    if not data:
        raise HTTPException(status_code=404, detail="No tasks found")
    return data


@router.post("/", response_model=schemas.Task, status_code=201)
def create_task(model: schemas.TaskCreate, db: db_dependency):
    """Create a new task."""
    new_task = models.Task(**model.model_dump())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


@router.get("/{task_id}", response_model=schemas.Task)
def fetch_task(task_id: int, db: db_dependency):
    """Fetch a single task by ID."""
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.put("/{task_id}", response_model=schemas.Task)
def update_task(task_id: int, model: schemas.TaskUpdate, db: db_dependency):
    """Update a task by ID."""
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    update_data = model.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(task, key, value)

    db.commit()
    db.refresh(task)
    return task


@router.delete("/{task_id}", status_code=204)
def delete_task(task_id: int, db: db_dependency):
    """Delete a task by ID."""
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()
    return None
