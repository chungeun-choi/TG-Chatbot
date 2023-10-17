from typing import Any, Optional

from sqlalchemy.orm import Session

from app.service.base import CRUDBase
from app.models.tgday import TGDay
from app.schemas.tgday import TGDayCreate,TGDayUpdate


class CRUDTGDay(CRUDBase[TGDay, TGDayCreate, TGDayUpdate]):
    def get(self, db: Session, user_id: Any) -> Optional[TGDay]:
        return db.query(self.TGDay).filter(self.TGDay.user_id == user_id).first()


tgday = CRUDTGDay(TGDay)