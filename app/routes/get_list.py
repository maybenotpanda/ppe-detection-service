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

@router.get("/")
def list_detections(db: Session = Depends(get_db)):
    return log_controller.get_list(db)
