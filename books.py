from fastapi import FastAPI

app = FastAPI()

BOOKS = {
    'book_1': {'title': 'title one', 'author': 'author one'},
    'book_2': {'title': 'title two', 'author': 'author two'},
    'book_3': {'title': 'title two', 'author': 'author two'},
    'book_4': {'title': 'title two', 'author': 'author two'},
    'book_5': {'title': 'title two', 'author': 'author two'},
    'book_6': {'title': 'title two', 'author': 'author two'},
    'book_7': {'title': 'title two', 'author': 'author two'},
    'book_8': {'title': 'title 8', 'author': 'author two'},
    'book_9': {'title': 'title 9', 'author': 'author two'},
    'book_10': {'title': 'title 10', 'author': 'author two'}
}


@app.get("/")
async def read_all_books():
    return BOOKS

@app.get("/books/{book_title}")
async def read_a_book(book_title):
    return BOOKS[book_title]



