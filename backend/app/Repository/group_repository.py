from sqlalchemy.exc import IntegrityError
from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.orm import Session
from backend.app.Repository.Interfaces.faction_interface import IFaction
from backend.app.models.faction import Group


class GroupRepository(IFaction):
    """Repository Queries for everthing faction"""

    # Scalar selects the whole enetity or just one row of data
    # Execute selects  individual rows of data or raw data

    def __init__(self, db: Session):
        """Inject db instance in the constructor"""
        self.db = db

    def save(self, entity: Group) -> Group:
        try:
            self.db.add(entity)
            self.db.commit()
            self.db.refresh(entity)
            return entity
        except IntegrityError as e:
            raise ValueError("Group Already Exist") from e
        except Exception as error:
            raise ValueError(f"Something went Wrong {error}") from error

    def get_all(self) -> List[Group]:
        return self.db.scalars(select(Group)).all()

    def get_by_id(self, group_id: int) -> Optional[Group]:
        result = self.db.scalars(select(Group).where(Group.id == group_id)).one_or_none()

        if not result:
            raise ValueError("Group not Found")
        
        return result
