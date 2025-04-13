from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, crud
from ..database import get_db

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/", response_model=schemas.TaskOut)
def create(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task)

@router.get("/", response_model=List[schemas.TaskOut])
def get_all(skip: int = 0, limit: int = Query(default=10, lte=100), db: Session = Depends(get_db)):
    return crud.get_tasks(db, skip, limit)

@router.put("/{task_id}", response_model=schemas.TaskOut)
def update(task_id: str, task: schemas.TaskUpdate, db: Session = Depends(get_db)):
    return crud.update_task(db, task_id, task)

@router.delete("/{task_id}")
def delete(task_id: str, db: Session = Depends(get_db)):
    return crud.delete_task(db, task_id)
