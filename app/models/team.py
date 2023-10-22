from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Sequence
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Team(Base):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    team_name = Column(String, index=True)
    manager_id = (Column(Integer, nullable=True),)
    users = relationship("User", back_populates="team")
