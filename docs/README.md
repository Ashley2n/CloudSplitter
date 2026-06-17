## Get Started

**Frontend**

```bash
    cd frontend/
```

```bash
    npm install
```

```bash
    npm run dev
```

Test

```bash
    npm test
```

**Backend**

```bash
    cd backend/
```

**_venv Command_**

Create

```bash
    python -m venv .venv
```

Run

```
	source .venv/Scripts/activate
```

Deactivate (Only when through)

```bash
    deactivate
```

<br>

Running Project

```bash
    pip install -r requirements.txt
```

Directory `backend/`

```bash
    fastapi dev app/main.py
```

### Backend Test

| Commands                             | Description                                                         |
| ------------------------------------ | ------------------------------------------------------------------- |
| pytest                               | Runs all discovered tests in the current directory.                 |
| pytest -v                            | Verbose mode: Shows individual test names and results.              |
| pytest tests/test_file.py            | Runs tests in a specific file.                                      |
| pytest tests/test_file.py::test_func | Runs a specific test function.                                      |
| pytest -k "keyword"                  | Runs tests matching a keyword expression (e.g., "user" or "login"). |
| pytest --cov=src                     | Generates a coverage report (requires pytest-cov).                  |
| pytest -s                            | Shows print statements output during test execution                 |

