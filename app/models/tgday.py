from sqlalchemy import Column, Integer, ForeignKey, DateTime, func
from app.db.base_class import Base


class TGDay(Base):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    regist_day = Column(DateTime, nullable=True)
    created_at = Column(
        DateTime,
        default=func.now(),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )
    updated_at = Column(
        DateTime,
        default=func.now(),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )
