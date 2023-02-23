from pydantic import BaseModel

class Book(BaseModel):
    title: str
    author: str
    isbn: str
    genre: str
    publication_date: str