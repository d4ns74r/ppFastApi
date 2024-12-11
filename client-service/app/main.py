from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas, db
import hashlib

app = FastAPI()


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def get_db():
    session = db.SessionLocal()
    try:
        yield session
    finally:
        session.close()


@app.on_event("startup")
def startup():
    # Создаем таблицы в базе данных при запуске приложения
    models.Base.metadata.create_all(bind=db.engine)


@app.post("/register/", response_model=schemas.UserResponse)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    if crud.get_user_by_username(db, user.username):
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(db, user)


@app.post("/login/")
def login(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, user.username)
    if db_user is None or db_user.password_hash != hash_password(user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"message": "Login successful"}


@app.get("/userInfo/{user_id}", response_model=schemas.UserResponse)
def get_user_info(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user_info(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
