from pymongo import MongoClient
from typing import List, Dict
import os

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017/")
DB_NAME = os.getenv("MONGO_DB", "books_db")
COLLECTION_NAME = "books"

client = MongoClient(MONGO_URL)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

def insert_books(books: List[Dict]):
    if books:
        collection.insert_many(books)

def find_books_by_category(category: str) -> List[Dict]:
    return list(collection.find({"category": category}))

def find_books_by_price(max_price: float) -> List[Dict]:
    return list(collection.find({"price": {"$lte": max_price}}))

# PostgreSQL integration using SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String, Float, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

POSTGRES_URL = os.getenv("POSTGRES_URL", "postgresql://postgres:postgres@localhost:5432/books_db")
engine = create_engine(POSTGRES_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class BookSQL(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    price = Column(Float)
    availability = Column(String)
    category = Column(String, index=True)
    description = Column(Text, nullable=True)
    summary = Column(Text, nullable=True)

def create_tables():
    Base.metadata.create_all(bind=engine)

def insert_books_sql(books):
    db = SessionLocal()
    for book in books:
        db_book = BookSQL(**book)
        db.add(db_book)
    db.commit()
    db.close()

def find_books_by_category_sql(category: str):
    db = SessionLocal()
    books = db.query(BookSQL).filter(BookSQL.category == category).all()
    db.close()
    return books

def find_books_by_price_sql(max_price: float):
    db = SessionLocal()
    books = db.query(BookSQL).filter(BookSQL.price <= max_price).all()
    db.close()
    return books
