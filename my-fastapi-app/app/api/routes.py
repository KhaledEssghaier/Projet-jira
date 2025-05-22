from fastapi import APIRouter, Query
from typing import List, Optional
from app.scraper import scrape_books
from app.models.book import insert_books, find_books_by_category, find_books_by_price
from app.schemas.book import Book
from app.llm import generate_summary
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse

router = APIRouter()

@router.post("/users/", response_model=UserResponse)
async def create_user(user: UserCreate):
    # Logic to create a new user
    pass

@router.get("/users/{user_id}", response_model=UserResponse)
async def read_user(user_id: int):
    # Logic to read a user by ID
    pass

@router.get("/users/", response_model=list[UserResponse])
async def read_users():
    # Logic to read all users
    pass

@router.post("/scrape", response_model=List[Book])
def scrape_and_store_books(url: str = Query(..., description="URL to scrape")):
    books = scrape_books(url)
    insert_books(books)
    return books

@router.get("/books", response_model=List[Book])
def get_books(category: Optional[str] = None, max_price: Optional[float] = None):
    if category:
        return find_books_by_category(category)
    if max_price is not None:
        return find_books_by_price(max_price)
    return []

@router.post("/summarize", response_model=str)
def summarize_book(description: str):
    return generate_summary(description)