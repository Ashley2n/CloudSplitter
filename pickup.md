# Sprint 1 - Group Management

## Sprint Goal

Build the foundation of the Expense Splitter API by allowing users to create groups and manage participants.

This sprint focuses on establishing the project structure, practicing Test-Driven Development (TDD), creating the initial database schema, and implementing the first business rules.

At the end of this sprint, users should be able to:

* Create a group
* Add participants to a group
* View participants within a group

No expense tracking should exist yet.

No settlement calculations should exist yet.

The objective is to build a solid foundation before introducing additional complexity.

---

# User Stories

## Story 1: Create Group

As a user, I want to create a group so that I can track shared expenses with other people.

### Acceptance Criteria

* User can create a group
* Group name is required
* Group name cannot be empty
* Group is stored in the database
* Group can be retrieved later

---

## Story 2: Add Participant

As a user, I want to add participants to a group.

### Acceptance Criteria

* Participant can be added to an existing group
* Participant name is required
* Participant name cannot be empty
* Duplicate participant names are not allowed within the same group
* Participant is stored in the database

---

## Story 3: View Participants

As a user, I want to see all participants in a group.

### Acceptance Criteria

* User can request a group's participants
* All participants belonging to the group are returned
* Empty groups return an empty participant list

---

# Domain Models

## Group

Properties:

* id
* name
* created_at

Relationship:

* One group contains many participants

---

## Participant

Properties:

* id
* group_id
* name
* created_at

Relationship:

* Participant belongs to one group

---

# Project Setup Tasks

## Repository Setup

* [X] Create repository
- [X] Create README.md
* [X] Create docs folder
* [X] Create pickup.md

---

## Backend Setup

* [X] Create backend directory
* [X] Create Python virtual environment
* [X] Configure pyproject.toml
* [X] Install FastAPI
* [X] Install Pytest
* [X] Configure test discovery
* [X] Verify tests can execute successfully

---

## Frontend Setup

* [X] Create React application
* [X] Configure TypeScript
* [ ] Install Vitest
* [ ] Verify test runner executes successfully

---

## Database Setup

* [ ] Configure SQLite database
* [ ] Create database connection
* [ ] Create initial migration strategy
* [ ] Verify database creation

---

# Backend Architecture Tasks

## Models

* [ ] Create Group model
* [ ] Create Participant model
* [ ] Configure relationships
* [ ] Verify database tables generate correctly

---

## Repository Layer

* [ ] Create Group repository
* [ ] Create Participant repository
* [ ] Create repository tests

Responsibilities:

* Save data
* Retrieve data
* Query data

No business logic should exist here.

---

## Service Layer

* [ ] Create Group service
* [ ] Create Participant service

Responsibilities:

* Validate business rules
* Coordinate repositories
* Raise domain errors

Business logic should exist here.

---

## API Layer

* [ ] Create create-group endpoint
* [ ] Create add-participant endpoint
* [ ] Create get-participants endpoint
* [ ] Validate request payloads
* [ ] Return appropriate status codes

API routes should remain thin.

---

# TDD Tasks

## Group Tests

Write tests before implementation.

* [ ] Group can be created
* [ ] Empty group name is rejected
* [ ] Whitespace-only group name is rejected

---

## Participant Tests

Write tests before implementation.

* [ ] Participant can be added
* [ ] Empty participant name is rejected
* [ ] Whitespace-only participant name is rejected
* [ ] Duplicate participant names are rejected
* [ ] Participant must belong to an existing group

---

## Integration Tests

* [ ] Create group endpoint succeeds
* [ ] Add participant endpoint succeeds
* [ ] Get participants endpoint succeeds

---

# API Endpoints

## Create Group

Purpose:

Create a new group.

Expected Result:

Returns newly created group information.

---

## Add Participant

Purpose:

Add participant to an existing group.

Expected Result:

Returns participant information.

---

## Get Participants

Purpose:

Retrieve participants belonging to a group.

Expected Result:

Returns participant collection.

---

# Definition of Done

Sprint 1 is complete when all of the following are true:

## Functionality

* [ ] User can create groups
* [ ] User can add participants
* [ ] User can retrieve participants

---

## Database

* [ ] Groups persist successfully
* [ ] Participants persist successfully
* [ ] Relationships function correctly

---

## Testing

* [ ] All unit tests pass
* [ ] All integration tests pass
* [ ] No failing tests remain

---

## Architecture

* [ ] API layer contains no business logic
* [ ] Business rules live in services
* [ ] Database access lives in repositories

---

## Code Quality

* [ ] No dead code
* [ ] No commented-out code
* [ ] No duplicate logic
* [ ] Naming is clear and consistent

---

# Out of Scope

The following items belong to future sprints and should not be implemented during Sprint 1:

* Expenses
* Balances
* Settlement calculations
* Authentication
* User accounts
* Authorization
* Payments
* Notifications
* Cloud deployment
* Docker
* CI/CD pipelines

If work begins on any of the above items, the sprint scope has expanded beyond its intended goal.
