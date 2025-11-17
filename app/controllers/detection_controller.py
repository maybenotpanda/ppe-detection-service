import os
import shutil
import string
import random
from datetime import datetime
from fastapi import UploadFile

from app.config.settings import settings
from app.utils.process_image import process_image
from app.controllers import log_controller

def random_id(length=5):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

async def handle_upload(file: UploadFile, db):

    try:
        UPLOAD_DIR = settings.UPLOAD_DIR
        RESULT_DIR = settings.RESULT_DIR

        os.makedirs(UPLOAD_DIR, exist_ok=True)
        os.makedirs(RESULT_DIR, exist_ok=True)

        upload_rand = random_id()
        result_rand = random_id()
        timestamp = datetime.now().strftime("%Y%m%d")

        ext = os.path.splitext(file.filename or "file")[1].lower()

        if ext not in [".jpg", ".jpeg", ".png", ".pdf"]:
            return {
                "status": "error",
                "message": "File format not supported. Only JPG, PNG, PDF allowed."
            }

        filename = f"upload_{timestamp}_{upload_rand}{ext}"
        file_path = os.path.join(UPLOAD_DIR, filename)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        if ext == ".pdf":
            alert = "PDF file — YOLO skipped"
            result_final_path = ""
        else:
            yolo_output_path, alert = process_image(file_path)

            result_filename = f"result_{timestamp}_{result_rand}.jpg"
            result_final_path = os.path.join(RESULT_DIR, result_filename)

            if os.path.exists(yolo_output_path):
                os.replace(yolo_output_path, result_final_path)

        response = log_controller.create(
            db=db,
            filename=filename,
            result_image=result_final_path,
            alert=alert
        )

        return response

    except Exception as e:
        return {
            "status": "error",
            "message": f"Upload failed: {str(e)}"
        }
