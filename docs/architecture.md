# Architecture

## Architectural Style

Cloud Splitter follows a layered architecture.

```text
API Layer
    |
Service Layer
    |
Repository Layer
    |
Database
```

Each layer has a single responsibility.

---

## API Layer

Responsibilities:

* Receive HTTP requests
* Validate inputs
* Return HTTP responses
* Convert domain objects into response models

The API layer should not contain business logic.

---

## Service Layer

Responsibilities:

* Business rules
* Validation beyond basic request validation
* Balance calculations
* Settlement logic

The service layer coordinates repositories and contains the application's core behavior.

---

## Repository Layer

Responsibilities:

* Database access
* Query execution
* Data persistence

Repositories isolate SQLAlchemy from the rest of the application.

---

## Database Layer

Responsibilities:

* Persistent storage
* Relationships
* Constraints

Suggested entities:

* Group
* Participant
* Expense

---

## Dependency Flow

Allowed:

API -> Service -> Repository -> Database

Not Allowed:

API -> Database
API -> Repository
Service -> Database

This keeps the architecture maintainable and testable.
