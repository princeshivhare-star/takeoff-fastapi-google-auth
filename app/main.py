import os
import uuid
from fastapi import FastAPI, Request, Depends
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
from sqlalchemy.orm import Session
from dotenv import load_dotenv

from .database import Base, engine, SessionLocal
from .models import User
from .schemas import IDRequest
from .auth import oauth

load_dotenv()

app = FastAPI(title="TakeOff Talent Assignment")

app.add_middleware(
    SessionMiddleware,
    secret_key=os.getenv("SESSION_SECRET_KEY")
)

templates = Jinja2Templates(directory="app/templates")

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


@app.get("/login")
async def login(request: Request):
    redirect_uri = os.getenv("BASE_URL") + "/auth/callback"
    return await oauth.google.authorize_redirect(request, redirect_uri)


@app.get("/auth/callback")
async def auth_callback(request: Request, db: Session = Depends(get_db)):
    token = await oauth.google.authorize_access_token(request)
    user_info = token.get("userinfo")

    if not user_info:
        return {"error": "Google login failed"}

    google_id = user_info.get("sub")
    name = user_info.get("name")
    email = user_info.get("email")
    picture = user_info.get("picture")

    user = db.query(User).filter(User.google_id == google_id).first()

    if not user:
        user = User(
            generated_id=str(uuid.uuid4())[:8],
            name=name,
            email=email,
            google_id=google_id,
            profile_photo_url=picture
        )
        db.add(user)
        db.commit()
        db.refresh(user)

    request.session["user_id"] = user.generated_id

    return RedirectResponse(url="/dashboard")


@app.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request, db: Session = Depends(get_db)):
    generated_id = request.session.get("user_id")

    if not generated_id:
        return RedirectResponse(url="/")

    user = db.query(User).filter(User.generated_id == generated_id).first()

    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={"user": user}
    )


@app.post("/api/user")
def get_user_by_generated_id(data: IDRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.generated_id == data.generated_id).first()

    if not user:
        return {"message": "Try Again"}

    return {
        "name": user.name,
        "email": user.email,
        "google_id": user.google_id,
        "profile_photo_url": user.profile_photo_url,
        "generated_id": user.generated_id
    }


@app.get("/logout")
def logout(request: Request):
    request.session.clear()
    return RedirectResponse(url="/")