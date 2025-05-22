from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Book Scraper & LLM Summary API")

app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Welcome to my FastAPI application!"}