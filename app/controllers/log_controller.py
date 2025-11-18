from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.logs import Logs
from app.schemas import log_schemas

def create(db: Session, user: str, filename: str, result_image: str, alert: str):
    try:
        log_data = Logs(
            user=user,
            filename=filename,
            result_image=result_image,
            alert=alert
        )

        db.add(log_data)
        db.commit()
        db.refresh(log_data)

        return {
            "status": "success",
            "message": "Detection saved successfully",
            "data": log_schemas.DetectionResponse.from_orm(log_data)
        }

    except Exception as e:
        db.rollback()
        return {
            "status": "error",
            "message": f"Failed to create detection: {str(e)}"
        }


def get_list(db: Session):
    try:
        detections = db.query(Logs).all()

        return {
            "status": "success",
            "data": detections
        }

    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to fetch detections: {str(e)}"
        }


def get_detail(db: Session, detection_id: int):
    try:
        detection = db.query(Logs).filter(Logs.id == detection_id).first()

        if not detection:
            return {
                "status": "error",
                "message": "Detection not found"
            }

        return {
            "status": "success",
            "data": detection
        }

    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to fetch detection: {str(e)}"
        }
