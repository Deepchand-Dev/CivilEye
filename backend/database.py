# SQLAlchemy se database engine banane ke liye
from sqlalchemy import create_engine

# Database ke sessions banane ke liye
from sqlalchemy.orm import sessionmaker, declarative_base


# SQLite database ka location/name
# "civic_eye.db" naam ki database file banegi
DATABASE_URL = "sqlite:///./civic_eye.db"


# Database ke saath connection establish karta hai
engine = create_engine(
    DATABASE_URL,

    # SQLite ko multiple requests ke saath safely use karne ke liye
    connect_args={"check_same_thread": False}
)


# Database session banane ka setup
# Session ka use database me data read/write karne ke liye hoga
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Database tables ke models banane ke liye Base class
# Baad me Complaint model isi Base se banega
Base = declarative_base()