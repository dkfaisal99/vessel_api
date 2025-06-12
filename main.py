# --- main.py ---
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database.db import SessionLocal, engine
import models
from crud import engine as engine_crud, gps as gps_crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/engine-data/")
def post_engine_data(engine_name: str, consumption: float, db: Session = Depends(get_db)):
    return engine_crud.create_engine_data(db, engine_name, consumption)

@app.get("/engine-data/")
def read_all_engine_data(db: Session = Depends(get_db)):
    return engine_crud.get_all_engine_data(db)

@app.get("/engine-total/")
def read_total_engine_consumption(db: Session = Depends(get_db)):
    return engine_crud.get_total_consumption(db)

@app.post("/gps/")
def post_gps(lat: str, lon: str, db: Session = Depends(get_db)):
    return gps_crud.create_gps_data(db, lat, lon)

@app.get("/gps/latest")
def get_latest_gps(db: Session = Depends(get_db)):
    return gps_crud.get_latest_gps(db)
