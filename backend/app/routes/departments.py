from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import schemas
from app.models import models
from app.core.database import SessionLocal
from app.routes.auth import get_current_user, get_db
from typing import List

router = APIRouter()

@router.post("/", response_model=schemas.Department)
def create_department(dept: schemas.DepartmentCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    db_dept = db.query(models.Department).filter(models.Department.name == dept.name).first()
    if db_dept:
        raise HTTPException(status_code=400, detail="Department already exists")
    if not dept.name or not dept.name.strip():
        raise HTTPException(status_code=400, detail="Department name is required")
    new_dept = models.Department(name=dept.name)
    db.add(new_dept)
    db.commit()
    db.refresh(new_dept)
    return new_dept

@router.get("/", response_model=List[schemas.Department])
def list_departments(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return db.query(models.Department).all()
