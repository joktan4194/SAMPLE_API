from typing import List
from fastapi import Depends, FastAPI, HTTPException, Request, Response, Path
from starlette.middleware.cors import CORSMiddleware
from . import schema, crud, models
from .db import SessionLocal, engine
import json
from array import array

from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)
ALLOWED_ORIGINS = '*'
app = FastAPI(
    title="User API",
    description="A Very Simple User API",
    version="1.0.0")

app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"]
)


# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def home_page():
    return {"Welcome"}


@app.post("/")
async def upload_users_from_csv_file(request: Request, db: Session = Depends(get_db)):
    req = await request.json()
    re = json.dumps(req)
    user = json.loads(re)
    return crud.create_batch(db, req)


@app.get("/v1/users/", response_model=List[schema.User])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_users(db, skip=skip, limit=limit)


@app.get("/v1/users/{id}", response_model=schema.User)
def get_user(id: int = Path(..., gt=0), db: Session = Depends(get_db)):
    db_user = crud.get_user(db, id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/v1/users/", response_model=schema.User)
def create_user(user: schema.User, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name(db, name=user.name, id=user.id)
    if db_user:
        raise HTTPException(
            status_code=400, detail="Name or ID already registered")
    return crud.create_user(db=db, user=user)

# app.include_router(users.router, prefix="/users", tags=["Users"])
