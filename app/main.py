from fastapi import FastAPI, HTTPException
from app.models import Book
from datetime import date

app = FastAPI()

books_db = {
    "0747532745": Book(title="Harry Potter and the Philosopher’s Stone", author="J.K. Rowling", isbn="0747532745", genre="Fantasy", publication_date="1997-06-26"),
    "054792822X": Book(title="The Hobbit", author="J.R.R. Tolkien", isbn="054792822X", genre="fiction", publication_date="1937-09-21"),
}
    
    
@app.get("/books")
def get_all_books():
    return {"books": books_db}

@app.post("/books")
def create_book(book: Book):
    if book.isbn in books_db:  
        raise HTTPException(status_code=400, detail="book already exists")
    books_db[book.isbn] = book
    return {"message": "Book added successfully"}


@app.get("/books/{isbn}")
def get_book_by_isbn(isbn: str):
    if isbn not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")
    return books_db[isbn]

@app.put("/books/{isbn}")
def update(isbn: str, book: Book):
    if isbn not in books_db:
        HTTPException(status_code=404, detail="Book does not exist.")
    
    book_to_update = book.dict(exclude_unset=True)

    current_book = books_db[isbn]
    for field, value in book_to_update.items():
        setattr(current_book, field, value)

    return {"message": "Book updated."}

@app.delete("/books/{isbn}")
def delete_book(isbn: str):
    if isbn not in books_db:
        raise HTTPException(status_code=404, detail="Book does not exist")
    books_db.pop(isbn)
    return {"message": "Book deleted successfully"}
