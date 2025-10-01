from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped


class Base(DeclarativeBase):
    pass


class Character(Base):
    __tablename__ = "character"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    
    def __repr__(self):
        return f"Character: {self.id}"
    
    
class PickedCharacter(Base):
    __tablename__ = "picked_character"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    date: Mapped[datetime]
    character_id: Mapped[int] = mapped_column(ForeignKey("character.id"))
    
    def __repr__(self):
        return f"Character: {self.id}, time_add: {self.date} "