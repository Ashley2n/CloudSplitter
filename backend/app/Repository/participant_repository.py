from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.orm import Session
from backend.app.models.faction import Participant


class ParticipantRepository():
    """Repository Queries for everthing faction"""

    # Scalar selects the whole enetity or just one row of data
    # Execute selects  individual rows of data or raw data

    def __init__(self, db: Session):
        """Inject db instance in the constructor"""
        self.db = db

    def save(self, entity: Participant) -> Participant:
        self.db.add(entity)
        self.db.commit()
        self.db.refresh(entity)
        return entity

    def get_all(self) -> List[Participant]:
        return self.db.scalars(select(Participant)).all()

    def get_by_id(self, participant_id: int) -> Optional[Participant]:
        result = self.db.scalars(select(Participant).where(Participant.id == participant_id)).one_or_none()

        if not result:
            raise ValueError("Participant not Found")
        
        return result
