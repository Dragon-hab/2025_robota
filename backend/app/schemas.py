from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional
from datetime import datetime

class Token(BaseModel):
    access_token: str
    token_type: str = 'bearer'

class TokenPayload(BaseModel):
    sub: Optional[int] = None

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6)
    full_name: Optional[str] = None

class UserOut(BaseModel):
    id: int
    email: EmailStr
    full_name: Optional[str]
    is_active: bool
    is_admin: bool

    class Config:
        orm_mode = True

class EventBase(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    description: Optional[str] = None
    location: Optional[str] = None
    start_at: datetime
    end_at: Optional[datetime] = None
    capacity: Optional[int] = None

    @validator('end_at')
    def end_must_be_after_start(cls, v, values):
        if v and 'start_at' in values and v < values['start_at']:
            raise ValueError('end_at must be after start_at')
        return v

class EventCreate(EventBase):
    pass

class EventOut(EventBase):
    id: int
    organizer_id: Optional[int]
    created_at: datetime

    class Config:
        orm_mode = True

class RegistrationCreate(BaseModel):
    event_id: int
    attendee_name: Optional[str] = None

class RegistrationOut(BaseModel):
    id: int
    event_id: int
    user_id: int
    registered_at: datetime
    attendee_name: Optional[str]

    class Config:
        orm_mode = True

class FeedbackCreate(BaseModel):
    event_id: int
    rating: int = Field(..., ge=1, le=5)
    comment: Optional[str] = None

class FeedbackOut(BaseModel):
    id: int
    event_id: int
    user_id: int
    rating: int
    comment: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True
