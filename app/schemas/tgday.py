from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class TGDayBase(BaseModel):
    user_id: Optional[int] = None
    regist_day: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class TGDayCreate(TGDayBase):
    regist_day: Optional[datetime]


class TGDayUpdate(TGDayBase):
    pass

class TGDayInDBBase(TGDayBase):
    id: Optional[int] = None

    class Config:
        from_attributes = True

class TGDay(TGDayInDBBase):
    pass