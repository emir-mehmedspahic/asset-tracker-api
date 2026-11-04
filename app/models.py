from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from app.database import Base

class Asset(Base):
    __tablename__ = "assets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    asset_type = Column(String, nullable=False)  # e.g., "watch", "car", "hardware", "knife"
    estimated_value = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)