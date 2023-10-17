import datetime
from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException

from app import service, models, schemas
from app.api import deps


router = APIRouter()

@router.get("/", response_model=List[schemas.Team])
def read_tgday(
    db = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve users.
    """
    teams = service.tgday.get_multi(db, skip=skip, limit=limit)
    return teams

@router.post("/", response_model=schemas.TGDay)
def regist_tgday(
    *,
    db = Depends(deps.get_db),
    regist_day: str,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new user.
    """
    if regist_day:
        year, month, day = map(int,regist_day.split("-"))
        regist_day = datetime.datetime(year=year,month=month,day=day)
        user_in = schemas.TGDayUpdate(user_id=current_user.id, regist_day=regist_day)
    else:
        raise HTTPException(
            status_code=400, detail="Not entered datetime"
        )

    tgday = service.tgday.create(db=db,obj_in=user_in)

    return tgday

@router.put("/update", response_model=schemas.TGDay)
def update_user(
    *,
    db = Depends(deps.get_db),
    user_id: int,
    user_in: schemas.TGDayUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update a user.
    """
    tgday = service.tgday.get(db, user_id=user_id)
    if not tgday:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system",
        )
    tgday = service.tgday.update(db, db_obj=tgday, obj_in=user_in)
    return tgday
