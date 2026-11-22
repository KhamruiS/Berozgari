from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, get_db, Base
from models import Company, Experiences

Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get("/Companies")
def list_companies(db: Session = Depends(get_db)):
    return db.query(Company).all()

@app.post("/Companies")
def add_company(name: str, role: str = "", package: str = "", eligibility: str = "", db: Session = Depends(get_db)):
    c = Company(name=name, role=role, package=package, eligibility=eligibility)
    db.add(c)
    db.commit()
    db.refresh(c)
    return c

@app.post("/Experiences")
def add_experience(company_id: int, role: str, year: int, round_type: str, questions: str, tips: str, db: Session = Depends(get_db)):
    e = Experiences(company_id=company_id, role=role, year=year, round_type=round_type, questions=questions, tips=tips)
    db.add(e)
    db.commit()
    db.refresh(e)
    return e

@app.get("/Experiences")
def list_experiences(company_id: int = None, role: str = None, year: int = None, round_type: str = None, db: Session = Depends(get_db)):
    q = db.query(Experiences).filter(Experiences.status == "Pending")
    if company_id:
        q = q.filter(Experiences.company_id == company_id)
    if role:
        q = q.filter(Experiences.role == role)
    if year:
        q = q.filter(Experiences.year == year)
    if round_type:
        q = q.filter(Experiences.round_type == round_type)
    return q.all()