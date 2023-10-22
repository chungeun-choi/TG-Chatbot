from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException

from app import service, models, schemas
from app.api import deps
from app.core.config import settings


router = APIRouter()


@router.get("/", response_model=List[schemas.Team])
def read_teams(
    db=Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve users.
    """
    teams = service.team.get_multi(db, skip=skip, limit=limit)
    return teams


@router.post("/", response_model=schemas.Team)
def create_team(
    *,
    db=Depends(deps.get_db),
    user_in: schemas.TeamCreate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Create new user.
    """
    team = service.team.create(db=db, obj_in=user_in)

    return team


@router.put("/{team_id}", response_model=schemas.Team)
def update_user(
    *,
    db=Depends(deps.get_db),
    team_id: int,
    user_in: schemas.TeamUpdate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Update a user.
    """
    team = service.team.get(db, id=team_id)
    if not team:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system",
        )
    team = service.team.update(db, db_obj=team, obj_in=user_in)
    return team


@router.delete("/{team_id}", response_model=schemas.Team)
def delete_user(
    *,
    db=Depends(deps.get_db),
    team_id: int,
    user_in: schemas.UserUpdate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    team = service.team.remove(db, team_id)
    return team
