# Domain Model

## Group

Represents a collection of participants sharing expenses.

Attributes:

* id
* name
* created_at

Relationships:

* has many participants
* has many expenses

---

## Participant

Represents a person within a group.

Attributes:

* id
* group_id
* name

Relationships:

* belongs to group
* may create expenses

---

## Expense

Represents a payment made by a participant.

Attributes:

* id
* group_id
* participant_id
* description
* amount
* created_at

Relationships:

* belongs to group
* belongs to participant

---

## Example

Vacation Group

Participants:

* Alice
* Bob
* Charlie

Expenses:

* Alice paid $90 for dinner
* Bob paid $60 for gas

Total Expenses:

$150

Share Per Person:

$50

Balances:

* Alice is owed $40
* Bob is owed $10
* Charlie owes $50
