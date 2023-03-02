from pydantic import BaseModel
from datetime import date
from typing import Optional

class Book(BaseModel):
    title: str
    author: str
    isbn: str
    genre: Optional[str]
    publication_date: Optional[date]
