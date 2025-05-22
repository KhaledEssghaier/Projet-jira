from pydantic import BaseModel
from typing import Optional

class Book(BaseModel):
    title: str
    price: float
    availability: str
    category: str
    description: Optional[str] = None
    summary: Optional[str] = None
