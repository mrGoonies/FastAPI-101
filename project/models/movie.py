from pydantic import BaseModel, Field
from datetime import date

current_year = date.today()


class MovieInfo(BaseModel):
    title: str = Field(min_length=5, max_length=150)
    release_year: str
    genre: str = Field(min_length=5, max_length=75)
    director: str = Field(min_length=5, max_length=100)
    raiting: float = Field(ge=1.0, le=10.0)
    by_the_user: int = Field(ge=1)

    class Config:
        json_schema_extra = {
            "example": {
                "title": "empty",
                "release_year": current_year,
                "genre": "empty",
                "director": "empty",
                "raiting": 1.0,
                "by_the_user": 0,
            }
        }
