from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_password
from app.service.base import CRUDBase
from app.models.team import Team
from app.schemas.team import TeamCreate,TeamUpdate


class CRUDTeam(CRUDBase[Team, TeamCreate, TeamUpdate]):
    pass


team = CRUDTeam(Team)