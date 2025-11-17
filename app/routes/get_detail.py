from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.config.database import SessionLocal
from app.controllers import log_controller

router = APIRouter(prefix="/detections", tags=["Detections"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{detection_id}")
def get_detection(detection_id: int, db: Session = Depends(get_db)):
    return log_controller.get_detail(db, detection_id)
