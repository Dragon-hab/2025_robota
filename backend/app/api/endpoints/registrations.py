from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas
from app.db.session import get_db
from app.core import security
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/api/auth/token')

router = APIRouter()

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = security.decode_access_token(token)
        user_id = int(payload.get('sub'))
    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid token')
    from app import crud as _crud
    user = _crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='User not found')
    return user

@router.post('/', response_model=schemas.RegistrationOut, status_code=status.HTTP_201_CREATED)
def register(reg_in: schemas.RegistrationCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    ev = crud.get_event(db, reg_in.event_id)
    if not ev:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Event not found')
    reg = crud.register_user(db, reg_in.event_id, current_user.id, reg_in.attendee_name)
    return reg

@router.get('/event/{event_id}', response_model=List[schemas.RegistrationOut])
def list_regs(event_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    # For demo, allow any authenticated user to list; in prod restrict to organizer/admin
    return crud.list_registrations_for_event(db, event_id)
