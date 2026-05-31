# Cloud Expense Splitter

A full-stack expense sharing application built with React, TypeScript, FastAPI, and Python. The application allows groups to record shared expenses and automatically calculate balances and settlement recommendations.

The primary goal of this project is to practice Test-Driven Development (TDD), clean architecture principles, API design, and cloud deployment.

---

## Project Goals

This project was built to demonstrate:

* Test-Driven Development (TDD)
* Clean Architecture
* REST API Design
* Frontend and Backend Integration
* TypeScript Development
* Python Development
* Automated Testing
* Cloud Deployment Fundamentals

---

## Features

### Group Management

* Create expense groups
* Add participants to groups
* View group members

### Expense Tracking

* Record expenses
* Associate expenses with participants
* Validate expense data

### Balance Calculation

* Calculate total spending
* Calculate individual contributions
* Determine participant balances

### Settlement Generation

* Calculate who owes money
* Generate simplified settlement recommendations
* Minimize repayment transactions

---

## Example

### Expenses

| Participant | Amount Paid |
| ----------- | ----------- |
| Alice       | $120        |
| Bob         | $30         |
| Charlie     | $50         |

### Result

Total Expenses: $200

Each Participant Share: $66.67

Settlement Recommendations:

* Bob owes Alice $36.67
* Charlie owes Alice $16.67

---

## Technology Stack

### Frontend

* React
* TypeScript
* Tailwind CSS
* Vitest
* React Testing Library

### Backend

* Python
* FastAPI
* Pytest
* Pydantic

### Database

* SQLite (Development)
* PostgreSQL (Optional Production)

### Cloud

* AWS S3
* AWS Lambda
* AWS API Gateway

---

## Architecture

The application follows a layered architecture to separate business logic from infrastructure concerns.

```text
Frontend (React)
        |
        v
REST API (FastAPI)
        |
        v
Application Services
        |
        v
Repository Layer
        |
        v
Database
```

### Why This Architecture?

* Business rules remain independent of frameworks
* Easier testing
* Easier maintenance
* Better scalability
* Clear separation of concerns

---

## Project Structure

```text
expense-splitter/
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── hooks/
│   │   ├── types/
│   │   └── tests/
│   │
│   └── package.json
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── services/
│   │   ├── repositories/
│   │   ├── models/
│   │   └── tests/
│   │
│   └── requirements.txt
│
├── docs/
│
└── README.md
```

---

## Test-Driven Development Workflow

Every feature is developed using the Red-Green-Refactor cycle.

### Red

Write a failing test.

### Green

Write the minimal amount of code necessary to make the test pass.

### Refactor

Improve the implementation while keeping tests green.

---

## Testing Strategy

### Unit Tests

Focus on business rules such as:

* Expense validation
* Balance calculations
* Settlement generation

### Integration Tests

Verify:

* API endpoints
* Database interactions
* Service communication

### Frontend Tests

Verify:

* User interactions
* Component rendering
* API integration

---

## MVP Roadmap

### Phase 1

Group Management

* Create groups
* Add participants

### Phase 2

Expense Management

* Record expenses
* Validate input

### Phase 3

Balance Calculation

* Calculate totals
* Determine participant balances

### Phase 4

Settlement Engine

* Generate repayment recommendations

### Phase 5

Frontend Integration

* Forms
* Expense display
* Settlement display

### Phase 6

Cloud Deployment

* Deploy frontend
* Deploy backend
* Configure API communication

---

## Future Enhancements

Potential future improvements include:

* User authentication
* Persistent user accounts
* Multi-group support
* Expense categories
* CSV exports
* Real-time updates
* Email notifications
* Mobile responsive enhancements

---

## Lessons Learned

This project focuses on applying software engineering fundamentals rather than building a large feature-rich application.

Key areas of learning include:

* Test-Driven Development
* Clean Architecture
* Dependency Management
* API Design
* Cloud Fundamentals
* Full-Stack Development

---

## License

This project is intended for educational and portfolio purposes.
