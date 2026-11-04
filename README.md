# Asset Tracker API

A small FastAPI backend for tracking personal assets (watches, cars, hardware, knives) and their estimated values, stored in SQLite through the SQLAlchemy ORM.

This is the first project in my FastAPI series. The follow-up, [gym-progress-api](https://github.com/emir-mehmedspahic/gym-progress-api), adds JWT authentication, nested relational data and a pytest suite.

## Tech stack

FastAPI, SQLAlchemy, SQLite, Pydantic.

## Project structure

```
app/
├── main.py       # FastAPI app and route handlers
├── models.py     # SQLAlchemy database tables
├── schemas.py    # Pydantic request/response validation
└── database.py   # Database connection and session handling
```

## Setup

```bash
python -m venv venv
source venv/bin/activate        # Windows PowerShell: .\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Running

```bash
python -m uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000/docs to try the endpoints in Swagger UI. The SQLite file `asset_tracker.db` is created on first start and is git-ignored.

## Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/assets/` | List all assets |
| POST | `/assets/` | Create an asset |

Example `POST /assets/` body:

```json
{
  "name": "Orient Kamasu",
  "asset_type": "watch",
  "estimated_value": 280.0
}
```
