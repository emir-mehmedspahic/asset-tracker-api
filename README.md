# Asset Tracker API

FastAPI backend with SQLite and SQLAlchemy ORM for tracking assets and valuations.

## Project Structure

- `app/main.py` - FastAPI app and route handlers
- `app/models.py` - SQLAlchemy database tables
- `app/schemas.py` - Pydantic request/response validation
- `app/database.py` - Database connection and session handling

## Setup & Running

1. Activate your virtual environment:
   ```powershell
   .\venv\Scripts\Activate.ps1

   Install dependencies:

Bash
pip install -r requirements.txt
Run the development server:

Bash
python -m uvicorn app.main:app --reload
Open http://127.0.0.1:8000/docs to test endpoints via Swagger UI.

Endpoints
GET /assets/ - Fetch all assets

POST /assets/ - Create a new asset

Example JSON payload for POST:

JSON
{
  "name": "Orient Kamasu",
  "asset_type": "watch",
  "estimated_value": 280.0
}

---

Once you save that file, commit and push it up:

```powershell
git add README.md
git commit -m "Update README formatting"
git push
