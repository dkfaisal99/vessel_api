# --- crud/engine.py ---
from sqlalchemy.orm import Session
from models import EngineData
from sqlalchemy import func


def create_engine_data(db: Session, engine_name: str, consumption: float):
    db_data = EngineData(engine_name=engine_name, consumption_liters=consumption)
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

def get_all_engine_data(db: Session):
    return db.query(EngineData).all()

def get_total_consumption(db: Session):
    return db.query(EngineData.engine_name, func.sum(EngineData.consumption_liters)).group_by(EngineData.engine_name).all()
