# SQLAlchemy se database ke column types import kar rahe hain
from sqlalchemy import Column, Integer, String, Float, DateTime

# database.py se Base import kar rahe hain
# Base ke through hum apna database table/model banayenge
from .database import Base

# Date aur time automatically save karne ke liye
from datetime import datetime


# Complaint database table
# Is class ka naam Complaint hai
class Complaint(Base):

    # Database table ka actual naam
    __tablename__ = "complaints"

    # Har complaint ka unique ID
    # primary_key=True means ye ID unique hogi
    id = Column(Integer, primary_key=True, index=True)

    # Uploaded image kahan save hui hai uska path
    image_path = Column(String, nullable=False)

    # Citizen ne complaint ke baare mein kya description diya
    description = Column(String, nullable=False)

    # Complaint ki location
    location = Column(String, nullable=False)

    # AI ne kaunsa issue identify kiya
    # Example: Pothole, Garbage, etc.
    issue_type = Column(String, nullable=True)

    # AI ka confidence score
    # Example: 0.87
    confidence = Column(Float, nullable=True)

    # Complaint ki severity
    severity = Column(String, nullable=True)

    # Complaint ka current status
    # Example: Reported, In Progress, Resolved
    status = Column(String, default="Reported")

    # Complaint create hone ka date aur time
    created_at = Column(DateTime, default=datetime.utcnow)