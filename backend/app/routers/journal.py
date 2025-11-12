from fastapi import APIRouter, HTTPException

from .. import models, schemas
from ..database import db_dependency

router = APIRouter(
    prefix="/api/v1/journal",
    tags=["Journals"],
)

# ===============================================================
# Dependencies
# ===============================================================
#
# this has been shifted to database.py
#
# ===============================================================
# JOURNAL OPERATIONS
# ===============================================================


@router.get("/", response_model=list[schemas.JournalEntry])
def get_all_entries(db: db_dependency):
    """Fetch all journal entries."""
    entries = db.query(models.JournalEntry).all()
    if not entries:
        raise HTTPException(status_code=404, detail="No journal entries found")
    return entries


@router.get("/{entry_id}", response_model=schemas.JournalEntry)
def get_single_entry(entry_id: int, db: db_dependency):
    """Fetch a single journal entry by ID."""
    entry = (
        db.query(models.JournalEntry).filter(models.JournalEntry.id == entry_id).first()
    )
    if not entry:
        raise HTTPException(status_code=404, detail="Journal entry not found")
    return entry


@router.post("/", response_model=schemas.JournalEntry, status_code=201)
def create_entry(entry: schemas.JournalCreate, db: db_dependency):
    """Create a new journal entry."""
    new_entry = models.JournalEntry(**entry.model_dump())
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return new_entry


@router.put("/{entry_id}", response_model=schemas.JournalEntry)
def update_entry(entry_id: int, entry_update: schemas.JournalUpdate, db: db_dependency):
    """Update an existing journal entry."""
    entry = (
        db.query(models.JournalEntry).filter(models.JournalEntry.id == entry_id).first()
    )
    if not entry:
        raise HTTPException(status_code=404, detail="Journal entry not found")

    update_data = entry_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(entry, key, value)

    db.commit()
    db.refresh(entry)
    return entry


@router.delete("/{entry_id}", status_code=204)
def delete_entry(entry_id: int, db: db_dependency):
    """Delete a journal entry."""
    entry = (
        db.query(models.JournalEntry).filter(models.JournalEntry.id == entry_id).first()
    )
    if not entry:
        raise HTTPException(status_code=404, detail="Journal entry not found")

    db.delete(entry)
    db.commit()
    return None
