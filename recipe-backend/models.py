from sqlalchemy import Column, Integer, String, JSON
from database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)


class Recipe(Base):
    __tablename__ = "recipes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    ingredients = Column(JSON)  # Store as JSON: {"ingredient": "quantity"}
    instructions = Column(String)
    portions = Column(Integer)


class UserHistory(Base):
    __tablename__ = "user_history"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    recipe_ids = Column(JSON)  # Store as JSON: [1, 2, 3]


if __name__ == "__main__":
    from database import engine
    from models import Base
    Base.metadata.create_all(bind=engine)
