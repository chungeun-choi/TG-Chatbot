from typing import Optional

from pydantic import BaseModel

class TeamBase(BaseModel):
    team_name: Optional[str] = None
    manager_id: Optional[int] = None


class TeamCreate(TeamBase):
    pass


class TeamUpdate(TeamBase):
    pass


class TeamInDBBase(TeamBase):
    id: Optional[int] = None

    class Config:
        from_attributes = True

class Team(TeamInDBBase):
    pass