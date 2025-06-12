# --- crud/gps.py ---
from sqlalchemy.orm import Session
from models import GPSData

def create_gps_data(db: Session, lat: str, lon: str):
    gps = GPSData(latitude=lat, longitude=lon)
    db.add(gps)
    db.commit()
    db.refresh(gps)
    return gps

def get_latest_gps(db: Session):
    return db.query(GPSData).order_by(GPSData.timestamp.desc()).first()