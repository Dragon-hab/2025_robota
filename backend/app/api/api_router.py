from fastapi import APIRouter
from .endpoints import auth, events, registrations, feedback

api_router = APIRouter()
api_router.include_router(auth.router, prefix='/auth', tags=['auth'])
api_router.include_router(events.router, prefix='/events', tags=['events'])
api_router.include_router(registrations.router, prefix='/registrations', tags=['registrations'])
api_router.include_router(feedback.router, prefix='/feedback', tags=['feedback'])
