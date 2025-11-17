from pydantic import BaseModel
from datetime import datetime

class DetectionCreate(BaseModel):
    filename: str
    result_image: str
    alert: str


class DetectionResponse(DetectionCreate):
    id: int
    created_at: datetime

    model_config = {
        "from_attributes": True
    }
