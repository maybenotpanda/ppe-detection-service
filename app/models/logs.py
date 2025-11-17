from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.config.database import Base

class Logs(Base):
    __tablename__ = "logs"
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String(255), nullable=False)
    result_image = Column(String(255), nullable=False)
    alert = Column(String(50))
    created_at = Column(DateTime, default=datetime.utcnow)
