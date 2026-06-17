

from typing import List

from backend.app.Repository.group_repository import GroupRepository
from backend.app.models.faction import Group, Participant
from backend.app.schemas.factions_schema import CreateGroup, GroupDto, ParticipantDto


class GroupService():

    def __init__(self, repository: GroupRepository):
        self._gr = repository

         
    def save_group(self, entity: CreateGroup):
        if(entity.name == "" or entity.name is None):
            raise ValueError("Name of CreateGroup is Empty")
        
        group = Group(name=entity.name)
        return self._gr.save(group)

    def find_group_by_id(self, groupId:int) -> GroupDto:
        group = self._gr.get_by_id(group_id=groupId)
        return GroupDto(id=group.id, name=group.name, participants=self.model_to_dto_participant_list(group.participants), created_at=group.created_at)


    def model_to_dto_participant_list(self, participants:List[Participant]) -> List[ParticipantDto]:
        """Converts a normal participants class to a list of ParticipantsDto class"""
        return [ParticipantDto(id=p.id, name=p.name, group_id=p.group_id, created_at=p.created_at) for p in participants]
