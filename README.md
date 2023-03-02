# Bookstore API

This is a RESTful API for a simple bookstore, built with FastAPI, a modern web framework for building APIs with Python. The API allows users to perform CRUD (Create, Read, Update, Delete) operations on a collection of books.

## Installation
1. Clone this repository:
    ```terminal
    git clone https://github.com/paouela-rapai/BookstoreApi.git
	cd <BookstoreApi>
    ```	
		
3. Create a virtual environment

    ```terminal
    python -m venv .venv
    ```

4. Activate virtual environment

    ```terminal
    source .venv/bin/activate
    ```

5. Install dependencies

    ```terminal
    pip intall -r requirements.txt    
    ```
 6.  Run the application: 
 
	```terminal
	uvicorn app.main:app --reload    
	```

## API Documantation
The API Documentation with the API routes, parameters and responses, can be accessed at `http://127.0.0.1:8000/docs`

## Endpoints
- #### GET /books
Returns a JSON object containing a list of all the books in the bookstore

- #### POST /books
Adds a new book to the bookstore. Requires a JSON object in the request body containing the details of the book

- #### GET /books/{isbn}
Returns a JSON object containing the details of the book with the specified ISBN

- #### PUT /books/{isbn}
Updates the details of the book with the specified ISBN. Requires a JSON object in the request body containing the fields to be updated

- #### DELETE /books/{isbn}
Deletes the book with the specified ISBN