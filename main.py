from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, get_db, Base
from models import Company

Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get("/companies")
def list_companies(db: Session = Depends(get_db)):
    return db.query(Company).all()

@app.post("/companies")
def add_company(name: str, role: str = "", package: str = "", eligibility: str = "", db: Session = Depends(get_db)):
    c = Company(name=name, role=role, package=package, eligibility=eligibility)
    db.add(c)
    db.commit()
    db.refresh(c)
    return c