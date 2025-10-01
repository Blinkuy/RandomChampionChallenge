from random import randint
from datetime import datetime, timezone

from sqlalchemy import desc, insert, values, select, delete , func
from sqlalchemy.orm import Session
from .database import engine

from .models import Character, PickedCharacter, Base
from .data import lis


def add_all():
    data = lis
    with Session(bind=engine) as session:
        stmt = insert(Character).values([{"name": name} for name in data])
        session.execute(stmt)
        session.commit()


def add_character():
    
    with Session(bind=engine) as session:
        MAX_ATTEMPTS=3000
        
        for _ in range(MAX_ATTEMPTS):
            random_id = randint(1, 171)
            stmt = select(PickedCharacter).where(PickedCharacter.character_id == random_id)
            existing = session.execute(stmt).first()

            if not existing:
                character = session.scalar(select(Character).where(Character.id == random_id))
                
                new_picked = PickedCharacter(
                    name = character.name,
                    date = datetime.now(timezone.utc),
                    character_id = character.id
                )
                session.add(new_picked)
                session.commit()
                
                break
        return character.name
    
    
def show_all():
    
    with Session(bind=engine) as session:
        return session.scalars(
            select(PickedCharacter).
            order_by(desc(PickedCharacter.date))
            ).all()


def get_characters() -> dict[str, dict]:
    subq = (
        select(
            PickedCharacter.id,
            PickedCharacter.character_id,
            PickedCharacter.date,
            func.row_number().over(
                partition_by=PickedCharacter.character_id,
                order_by=desc(PickedCharacter.date)
            ).label("row_num")
        )
        .subquery()
    )

    latest_picked = (
        select(subq.c.id, subq.c.character_id, subq.c.date)
        .where(subq.c.row_num == 1)
        .subquery()
    )

    query = (
        select(Character, latest_picked.c.id, latest_picked.c.date)
        .join(latest_picked, Character.id == latest_picked.c.character_id)
        .order_by(latest_picked.c.date.desc())
    )
    
    with Session(bind=engine) as session:
        result = session.execute(query).all()

    result_dict = {}
    for char, picked_id, picked_date in result:
        result_dict[char.name] = {
            "id": picked_id,        
            "date": picked_date.isoformat()
        }
    
    return result_dict

        
def drop_all():
    Base.metadata.drop_all(bind=engine)


def create_all():
    Base.metadata.create_all(bind=engine)
    



"""
with Session(bind=engine) as session:
    characters = get_characters_by_first_pick_order(session)
    for char in characters:
        print(char.name)
"""


"""
def get_character(id: int):
    
    with engine.connect() as connection:
        stmt = select(Character).where(Character.id == id)
        character = connection.execute(stmt).first()
        
        return character
"""