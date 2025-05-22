import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_scrape_and_store_books(monkeypatch):
    def mock_scrape_books(url):
        return [{
            'title': 'Test Book',
            'price': 10.0,
            'availability': 'In stock',
            'category': 'Test Category'
        }]
    monkeypatch.setattr('app.scraper.scrape_books', mock_scrape_books)
    response = client.post("/scrape", params={"url": "http://fake-url.com"})
    assert response.status_code == 200
    assert response.json()[0]['title'] == 'Test Book'

def test_summarize_book(monkeypatch):
    monkeypatch.setattr('app.llm.generate_summary', lambda desc: "Résumé")
    response = client.post("/summarize", json={"description": "A long description."})
    assert response.status_code == 200
    assert response.json() == "Résumé"
