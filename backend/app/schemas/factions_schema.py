from typing import List, Optional

from pydantic import BaseModel

class GroupDto(BaseModel):
    """Group Base Data Transfer Object"""
    id: int
    name:str
    participants: List['ParticipantDto']
    created_at: str

class CreateGroup(BaseModel):
    """Group Create or Request"""
    name: str

class UpdateGroupDto(BaseModel):
    """Group Update"""
    id: Optional[int] = None
    name: Optional[str] = None



class CreateParticipant(BaseModel):
    """Participants Create or Request"""
    group_id: Optional[int]
    name:str

class ParticipantDto(BaseModel):
    """Participants Reponse or Base"""
    id: int
    name: str
    group_id: int
    created_at: str

class UpdateParticipantsDto(BaseModel):
    """Participants Update Dto"""
    id:Optional[int] = None
    name:Optional[str] = None
    group_id:Optional[int] = None
 