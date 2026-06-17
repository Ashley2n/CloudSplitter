from abc import ABC, abstractmethod
from backend.app.models.faction import Group


class IFaction(ABC):
    """Faction Interface"""

    @abstractmethod
    def save(self, entity: Group) -> Group:
        """Save a group"""

    @abstractmethod
    def get_all(self) -> list[Group]:
        """Find all Groups"""

    def get_by_id(self, group_id: int) -> Group:
        """Get a Group by Id"""
