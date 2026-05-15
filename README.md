# FastAPI Google OAuth Assignment

A FastAPI based full stack web application with Google OAuth authentication and SQLite database integration.

This project was built for the TakeOff Talent Python Full Stack Web Development Intern assignment.

---

## Features

- Google OAuth Login
- FastAPI backend APIs
- SQLite database integration
- SQLAlchemy ORM
- Jinja2 frontend templates
- Attractive responsive UI
- Stores user details after successful Google login:
  - Name
  - Email
  - Google ID
  - Profile Photo URL
  - Unique Generated ID
- Fetch user details using generated ID
- Shows `"Try Again"` if generated ID does not exist
- Environment variable usage for secrets
- FastAPI Swagger API documentation

---

## Tech Stack

### Backend

- FastAPI
- SQLAlchemy
- SQLite
- Authlib
- Uvicorn
- Python Dotenv
- ItsDangerous
- HTTPX

### Frontend

- HTML
- CSS
- JavaScript
- Jinja2 Templates

### Authentication

- Google OAuth 2.0

### Deployment

- Vercel

---

## Project Structure

```txt
takeoff-fastapi-google-auth/
│── app/
│   │── main.py
│   │── database.py
│   │── models.py
│   │── schemas.py
│   │── auth.py
│   └── templates/
│       │── index.html
│       │── dashboard.html
│── .env
│── .gitignore
│── requirements.txt
│── vercel.json
│── README.md
```

---

## Local Setup Instructions

### 1. Clone Repository

```bash
git clone <your-github-repo-link>
cd takeoff-fastapi-google-auth
```

---

### 2. Create Virtual Environment

#### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Google OAuth Setup

### 1. Open Google Cloud Console

Open Google Cloud Console and create a new project.

---

### 2. Configure OAuth Consent Screen

Go to:

```txt
APIs & Services → OAuth consent screen
```

Select:

```txt
External
```

Fill required details:

- App name
- User support email
- Developer contact email

Save and continue.

---

### 3. Create OAuth Client ID

Go to:

```txt
APIs & Services → Credentials
```

Click:

```txt
Create Credentials → OAuth Client ID
```

Application type:

```txt
Web Application
```

For local development, add this Authorized Redirect URI:

```txt
http://localhost:8000/auth/callback
```

After deployment, also add your Vercel callback URL:

```txt
https://your-vercel-app.vercel.app/auth/callback
```

---

## Environment Variables

Create a `.env` file in the root directory.

```env
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
SESSION_SECRET_KEY=your_random_secret_key
BASE_URL=http://localhost:8000
```

For Vercel deployment, add the same variables in Vercel Project Settings.

For deployed app:

```env
BASE_URL=https://your-vercel-app.vercel.app
```

---

## Run Locally

```bash
uvicorn app.main:app --reload
```

Open:

```txt
http://localhost:8000
```

---

## Application Flow

```txt
User opens frontend
        ↓
Clicks Continue with Google
        ↓
Google OAuth login page opens
        ↓
Google redirects to /auth/callback
        ↓
Backend receives user info
        ↓
User details are stored in SQLite database
        ↓
A unique generated ID is created
        ↓
Dashboard displays user profile and generated ID
        ↓
User can search details using generated ID
```

---

## API Endpoint

### POST `/api/user`

Fetch user details using generated ID.

---

### Request Body

```json
{
  "generated_id": "abc12345"
}
```

---

### Success Response

```json
{
  "name": "Prince Shivhare",
  "email": "example@gmail.com",
  "google_id": "123456789",
  "profile_photo_url": "https://...",
  "generated_id": "abc12345"
}
```

---

### Failure Response

```json
{
  "message": "Try Again"
}
```

---

## FastAPI Swagger Docs

FastAPI automatically provides interactive API documentation.

Open:

```txt
http://localhost:8000/docs
```

For deployed app:

```txt
https://your-vercel-app.vercel.app/docs
```

---

## Database

Database used:

```txt
SQLite
```

Database file:

```txt
users.db
```

Note: `users.db` is ignored in GitHub using `.gitignore`.

---

## View Stored Data Locally

Open SQLite:

```bash
sqlite3 users.db
```

Show tables:

```sql
.tables
```

Show stored users:

```sql
SELECT * FROM users;
```

Exit SQLite:

```sql
.exit
```

---

## Vercel Deployment

### 1. Create `vercel.json`

```json
{
  "rewrites": [
    {
      "source": "/(.*)",
      "destination": "/app/main.py"
    }
  ]
}
```

---

### 2. Push Code to GitHub

```bash
git init
git add .
git commit -m "FastAPI Google OAuth assignment"
git branch -M main
git remote add origin <your-github-repo-link>
git push -u origin main
```

---

### 3. Import Project on Vercel

1. Open Vercel
2. Click `New Project`
3. Import your GitHub repository
4. Keep framework preset as default/other
5. Add environment variables

---

### 4. Add Environment Variables in Vercel

Go to:

```txt
Project Settings → Environment Variables
```

Add:

```env
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
SESSION_SECRET_KEY=your_random_secret_key
BASE_URL=https://your-vercel-app.vercel.app
```

---

### 5. Update Google OAuth Redirect URI

In Google Cloud Console, add:

```txt
https://your-vercel-app.vercel.app/auth/callback
```

---

### 6. Deploy

Click:

```txt
Deploy
```

After deployment, open your Vercel URL:

```txt
https://your-vercel-app.vercel.app
```

---

## Important Note About SQLite on Vercel

SQLite works properly for local development.

On Vercel serverless deployment, local file-based SQLite storage is not recommended for permanent production storage because serverless file systems are not persistent.

For production, a hosted database like PostgreSQL, Neon, Supabase, or Railway PostgreSQL is recommended.

For this assignment, SQLite is acceptable because it was recommended for simplicity.

---

## Screenshots

### Login Page

Add screenshot here.

### Google OAuth Login

Add screenshot here.

### Dashboard

Add screenshot here.

### API Response

Add screenshot here.

---

## Future Improvements

- PostgreSQL database for production deployment
- JWT based authentication
- Better error handling
- User session expiry handling
- Docker support
- Separate React frontend
- Deployment with persistent cloud database

---

## Author

Prince Shivhare

GitHub:  
https://github.com/princeshivhare-star


---

## Assignment Submission

This project was created as part of the TakeOff Talent Python Full Stack Web Development Internship Assignment.