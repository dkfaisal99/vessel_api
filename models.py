
# --- models.py ---
from sqlalchemy import Column, Integer, String, Float, DateTime
from database.db import Base
from datetime import datetime

class EngineData(Base):
    __tablename__ = "engine_data"
    id = Column(Integer, primary_key=True, index=True)
    engine_name = Column(String(50))
    date = Column(DateTime, default=datetime.utcnow)
    consumption_liters = Column(Float)

class GPSData(Base):
    __tablename__ = "gps_data"
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    latitude = Column(String(50))
    longitude = Column(String(50))
