from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import engine, Base, get_db
from app import models, schemas

# Create database tables automatically
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Asset & Performance Tracker API", version="0.1.0")

@app.post("/assets/", response_model=schemas.AssetResponse)
def create_asset(asset: schemas.AssetCreate, db: Session = Depends(get_db)):
    db_asset = models.Asset(**asset.model_dump())
    db.add(db_asset)
    db.commit()
    db.refresh(db_asset)
    return db_asset

@app.get("/assets/", response_model=List[schemas.AssetResponse])
def read_assets(db: Session = Depends(get_db)):
    return db.query(models.Asset).all()