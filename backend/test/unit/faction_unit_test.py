import pytest
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from backend.app.Repository.group_repository import GroupRepository
from backend.app.Repository.participant_repository import ParticipantRepository
from backend.app.models.faction import Group, Participant
from backend.app.schemas.factions_schema import CreateGroup
from backend.app.services.group_services import GroupService


def __init__(self, db: Session):
    self.db = db


def test_save_group_to_database(db_session):
    # Arrange
    repository = GroupRepository(db_session)
    new_group = Group(name="Sushi")

    # Act
    new_entity = repository.save(new_group)

    # Assert
    assert new_entity is not None
    assert new_entity.id is 1
    assert new_entity.name is new_group.name

def test_group_with_an_empty_name_should_not_save(db_session):
    # Arrange
    _gr = GroupRepository(db=db_session)
    _gs = GroupService(_gr)
    new_group = CreateGroup(name="")

    # Act
    with pytest.raises(ValueError):
        _gs.save_group(new_group)



def test_read_group_from_db(db_session):
    # Arrange
    repository = GroupRepository(db_session)
    sushi = Group(name="Sushi")
    repository.save(sushi)

    # Act
    result = repository.get_by_id(1)

    # Assert
    assert result.id is 1
    assert result.name is sushi.name


def test_read_not_found_with_Wrong_group_id(db_session):
    # Arrange
    repository = GroupRepository(db_session)
    sushi = Group(name="Sushi")
    repository.save(sushi)

    # Act

    # Assert
    with pytest.raises(ValueError):
        repository.get_by_id(-12)


# Participants Unit Test


def test_save_participant_to_database(db_session):
    # Arrange
    _pr = ParticipantRepository(db_session)
    _gr = GroupRepository(db_session)

    sushi = Group(name="Sushi")
    _gr.save(sushi)

    participant = Participant(name="Alice", group_id=sushi.id)

    # Act
    alice = _pr.save(participant)

    # Assert
    assert alice is not None
    assert alice.id is 1
    assert alice.name is participant.name

def test_invalid_participant_id_should_fail(db_session):
    # Arrange
    _pr = ParticipantRepository(db_session)
    _gr = GroupRepository(db_session)

    sushi = _gr.save(Group(name="Sushi"))
    _pr.save(Participant(name="Alice", group_id=sushi.id))

    # Act
    # Assert
    with pytest.raises(ValueError):
        _pr.get_by_id(-1)

    with pytest.raises(ValueError):
        _pr.get_by_id(100)

    
def test_should_reject_duplicate_participants(db_session):
     # Arrange
    _pr = ParticipantRepository(db_session)
    _gr = GroupRepository(db_session)

    # Act
    sushi = _gr.save(Group(name="Sushi"))
    _pr.save(Participant(name="Alice", group_id=sushi.id))

    # Assert
    with pytest.raises(IntegrityError):
        _pr.save(Participant(name="Alice", group_id=sushi.id))
