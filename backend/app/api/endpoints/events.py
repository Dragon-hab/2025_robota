from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas
from app.db.session import get_db

router = APIRouter()

@router.post('/', response_model=schemas.EventOut, status_code=status.HTTP_201_CREATED)
def create_event(event_in: schemas.EventCreate, db: Session = Depends(get_db)):
    ev = crud.create_event(db, event_in)
    return ev

@router.get('/', response_model=List[schemas.EventOut])
def list_events(skip: int = 0, limit: int = Query(100, le=100), db: Session = Depends(get_db)):
    return crud.list_events(db, skip=skip, limit=limit)

@router.get('/{event_id}', response_model=schemas.EventOut)
def get_event(event_id: int, db: Session = Depends(get_db)):
    ev = crud.get_event(db, event_id)
    if not ev:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Event not found')
    return ev
