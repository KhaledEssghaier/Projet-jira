import requests
from bs4 import BeautifulSoup
from typing import List, Dict

def scrape_books(url: str) -> List[Dict]:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    books = []
    for article in soup.select('article.product_pod'):
        title = article.h3.a['title']
        price = article.select_one('.price_color').text.strip().replace('£', '')
        availability = article.select_one('.availability').text.strip()
        category = soup.select_one('ul.breadcrumb li:nth-of-type(3) a').text.strip() if soup.select_one('ul.breadcrumb li:nth-of-type(3) a') else "Unknown"
        books.append({
            'title': title,
            'price': float(price),
            'availability': availability,
            'category': category
        })
    return books
