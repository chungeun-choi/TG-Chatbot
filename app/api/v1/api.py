from fastapi import APIRouter

from app.api.v1.endpoints import  login, user, team

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(user.router, prefix="/users", tags=["users"])
api_router.include_router(team.router, prefix="/teams", tags=["teams"])