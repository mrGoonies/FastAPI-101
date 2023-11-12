from models.movie import MovieInfo
from main import app


@app.get("/api/get-all-movies", tags=["movies"])
def get_all_movies() -> dict:
    return {"Movies": "all movies"}
