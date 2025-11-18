from fastapi import APIRouter, UploadFile, Form, File, Depends
from sqlalchemy.orm import Session

from app.config.database import SessionLocal
from app.controllers import detection_controller

router = APIRouter(prefix="/detections", tags=["Detections"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/upload")
async def upload_detection(file: UploadFile = File(...), user: str = Form(...), db: Session = Depends(get_db)):
    return await detection_controller.handle_upload(file, user, db)