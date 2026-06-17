 Implementation: Updating Participants via a Dedicated Endpoint
Instead of putting groupIds or a participant list inside UpdateGroupDto, the standard RESTful approach is to manage participants via their own endpoint or a specific sub-resource endpoint. This separates concerns: Group management vs. Membership management. 

Here is how the API and Service layer should look for this pattern:

A. The DTOs
Keep UpdateGroupDto simple (only group properties). Create a specific DTO for managing membership. 

class UpdateGroupDto(BaseModel):
    name: Optional[str] = None
    # No participant list here

class GroupMembershipUpdate(BaseModel):
    """Specific DTO for adding/removing participants"""
    participant_ids: List[int] # The list of IDs to set as the new members

B. The API Endpoint (FastAPI Example)
Create a dedicated endpoint to update the relationship. This is often a PUT (replace all) or PATCH (add/remove) on a sub-path. 

@app.put("/groups/{group_id}/participants")
async def update_group_participants(
    group_id: int, 
    membership: GroupMembershipUpdate, 
    service: GroupService = Depends()
):
    """
    Replaces the entire list of participants for a group.
    """
    updated_group = service.update_participants(group_id, membership.participant_ids)
    return service.get_group_by_id(group_id) # Returns full GroupDto

C. The Service Layer Logic
This is where the manual syncing happens. You load the group, clear the old relationships, and assign the new ones. 

class GroupService:
    def update_participants(self, group_id: int, new_participant_ids: List[int]) -> Group:
        # 1. Fetch Group and Participants
        group = self.session.get(Group, group_id)
        if not group:
            raise HTTPException(404, "Group not found")
        
        # 2. Fetch the new participant objects
        new_participants = (
            self.session.query(Participant)
            .filter(Participant.id.in_(new_participant_ids))
            .all()
        )
        
        # 3. Validate count (optional safety check)
        if len(new_participants) != len(new_participant_ids):
            raise HTTPException(400, "One or more participant IDs are invalid")

        # 4. Sync Relationship (SQLAlchemy handles the FK updates)
        # This automatically sets participant.group_id for new ones 
        # and NULLs it for removed ones (if cascade allows) or deletes them.
        group.participants = new_participants
        
        self.session.commit()
        self.session.refresh(group)
        return group

    def get_group_by_id(self, group_id: int) -> GroupDto:
        # 1. Query with Eager Loading (Critical for nested DTOs)
        stmt = select(Group).options(selectinload(Group.participants)).where(Group.id == group_id)
        db_group = self.session.execute(stmt).scalar_one_or_none()
        
        if not db_group:
            raise HTTPException(404, "Group not found")

        # 2. Manual Mapping (Your original idea)
        # You must manually convert the nested list
        participant_dtos = [
            ParticipantDto(
                id=p.id, 
                name=p.name, 
                group_id=p.group_id, 
                created_at=p.created_at
            ) 
            for p in db_group.participants
        ]

        return GroupDto(
            id=db_group.id,
            name=db_group.name,
            created_at=db_group.created_at,
            participants=participant_dtos # Pass the manually created list
        )

Summary of Changes
Remove from_attributes=True if you strictly manually map everything (optional but cleaner). 
Keep List['ParticipantDto'] in your Read DTO; it defines the structure of the nested data.
Manual Mapping: You must explicitly loop through db_group.participants and create ParticipantDto instances before passing them to GroupDto. 
Update Strategy: Do not put participant lists in UpdateGroupDto. Use a dedicated endpoint (PUT /groups/{id}/participants) and a specific DTO (GroupMembershipUpdate) to handle the relationship logic cleanly. 