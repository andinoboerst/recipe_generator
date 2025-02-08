from pydantic import BaseModel


class RecipeBase(BaseModel):
    name: str
    ingredients: dict
    instructions: str
    portions: int


class RecipeCreate(RecipeBase):
    pass


class Recipe(RecipeBase):
    id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
