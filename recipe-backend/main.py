from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas, auth
from .database import SessionLocal, engine

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/register/", response_model=schemas.User)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(db=db, user=user)


@app.post("/token/")
def login():
    # Implement JWT token generation
    pass


@app.get("/recipes/")
def get_recipes(n: int, portions: int, db: Session = Depends(get_db)):
    recipes = crud.get_random_recipes(db, n)
    shopping_list = generate_shopping_list(recipes, portions)
    return {"recipes": recipes, "shopping_list": shopping_list}
