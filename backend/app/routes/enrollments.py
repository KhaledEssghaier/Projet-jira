from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import schemas
from app.models import models
from app.core.database import SessionLocal
from app.routes.auth import get_current_user, get_db

router = APIRouter()

@router.post("/", response_model=schemas.Enrollment)
def enroll_student(enrollment: schemas.EnrollmentCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    student = db.query(models.User).get(enrollment.student_id)
    formation = db.query(models.Formation).get(enrollment.formation_id)
    if not student or not formation:
        raise HTTPException(status_code=404, detail="Student or Formation not found")
    if formation in student.formations:
        raise HTTPException(status_code=400, detail="Student already enrolled in this formation")
    student.formations.append(formation)
    db.commit()
    return {"student_id": student.id, "formation_id": formation.id}
