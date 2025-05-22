from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import schemas
from app.models import models
from app.core.database import SessionLocal
from app.routes.auth import get_current_user, get_db
from typing import List

router = APIRouter()

@router.post("/", response_model=schemas.Formation)
def create_formation(formation: schemas.FormationCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    new_formation = models.Formation(theme=formation.theme, description=formation.description)
    db.add(new_formation)
    db.commit()
    db.refresh(new_formation)
    return new_formation

@router.get("/", response_model=List[schemas.Formation])
def list_formations(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return db.query(models.Formation).all()

@router.get("/{formation_id}", response_model=schemas.Formation)
def get_formation(formation_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    formation = db.query(models.Formation).get(formation_id)
    if not formation:
        raise HTTPException(status_code=404, detail="Formation not found")
    return formation

@router.put("/{formation_id}", response_model=schemas.Formation)
def update_formation(formation_id: int, formation: schemas.FormationCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    db_formation = db.query(models.Formation).get(formation_id)
    if not db_formation:
        raise HTTPException(status_code=404, detail="Formation not found")
    db_formation.theme = formation.theme
    db_formation.description = formation.description
    db.commit()
    db.refresh(db_formation)
    return db_formation

@router.delete("/{formation_id}")
def delete_formation(formation_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    db_formation = db.query(models.Formation).get(formation_id)
    if not db_formation:
        raise HTTPException(status_code=404, detail="Formation not found")
    db.delete(db_formation)
    db.commit()
    return {"detail": "Formation deleted"}
