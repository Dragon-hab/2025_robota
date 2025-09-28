from sqlalchemy.orm import Session
from app import models, schemas
from app.core.security import get_password_hash

# User CRUD
def create_user(db: Session, user_in: schemas.UserCreate):
    hashed = get_password_hash(user_in.password)
    user = models.User(email=user_in.email, full_name=user_in.full_name, hashed_password=hashed)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

# Events
def create_event(db: Session, event_in: schemas.EventCreate, organizer_id: int | None = None):
    ev = models.Event(**event_in.dict(), organizer_id=organizer_id)
    db.add(ev)
    db.commit()
    db.refresh(ev)
    return ev

def list_events(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Event).offset(skip).limit(limit).all()

def get_event(db: Session, event_id: int):
    return db.query(models.Event).filter(models.Event.id == event_id).first()

# Registrations
def register_user(db: Session, event_id: int, user_id: int, attendee_name: str | None = None):
    # prevent duplicate registrations
    exists = db.query(models.Registration).filter(models.Registration.event_id==event_id, models.Registration.user_id==user_id).first()
    if exists:
        return exists
    reg = models.Registration(event_id=event_id, user_id=user_id, attendee_name=attendee_name)
    db.add(reg)
    db.commit()
    db.refresh(reg)
    return reg

def list_registrations_for_event(db: Session, event_id: int):
    return db.query(models.Registration).filter(models.Registration.event_id==event_id).all()

# Feedback
def create_feedback(db: Session, feedback_in: schemas.FeedbackCreate, user_id: int):
    fb = models.Feedback(**feedback_in.dict(), user_id=user_id)
    db.add(fb)
    db.commit()
    db.refresh(fb)
    return fb

def list_feedback_for_event(db: Session, event_id: int):
    return db.query(models.Feedback).filter(models.Feedback.event_id==event_id).all()
