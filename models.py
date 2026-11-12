from sqlalchemy import Column, Integer, String, Text, ForeignKey
from database import Base

class Company(Base):
    __tablename__ = "Companies"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    role = Column(String)
    package = Column(String)
    eligibility = Column(String)

class Experiences(Base):
    __tablename__ = "Experiences"
    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey("Companies.id"))
    role = Column(String)
    year = Column(Integer)
    round_type = Column(String)
    questions = Column(Text)
    tips = Column(Text)
    status = Column(String, default="Pending")