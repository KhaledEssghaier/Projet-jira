import pytest
from app.scraper import scrape_books

def test_scrape_books():
    url = "http://books.toscrape.com/catalogue/category/books/science_22/index.html"
    books = scrape_books(url)
    assert isinstance(books, list)
    if books:
        book = books[0]
        assert 'title' in book
        assert 'price' in book
        assert 'availability' in book
        assert 'category' in book
