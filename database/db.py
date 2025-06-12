# --- database/db.py ---
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ✅ PostgreSQL connection string for Render
SQLALCHEMY_DATABASE_URL = (
    "postgresql://vessel_db_0fm3_user:kGT7Rh63gkkGE5pO4nhu3OwGBDFyGwoc@dpg-d15a5n3uibrs73boj000-a.oregon-postgres.render.com/vessel_db_0fm3"
)

# Create the engine and session
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for ORM models
Base = declarative_base()
