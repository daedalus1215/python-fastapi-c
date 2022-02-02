from enum import Enum
from typing import Optional

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

class DirectionName(str, Enum):
    north = "North"
    south = "South"
    east = "East"
    west = "West"

@app.get("/")
async def read_all_books(skip_book: Optional[str] = None):
    if skip_book:
        new_books = BOOKS.copy()
        del new_books[skip_book]
        return new_books
    return BOOKS

@app.get("/books/{book_title}")
async def read_a_book(book_title):
    return BOOKS[book_title]

@app.get("/{book_name}")
async def read_book(book_name: str):
    return BOOKS[book_name]

@app.post("/")
async def create_book(book_title, book_author):
    current_book_id = 0
    if len(BOOKS) > 0:
        for book in BOOKS:
            x = int(book.split('_')[-1])
            if x > current_book_id:
                current_book_id = x
    BOOKS[f'book_{current_book_id + 1}'] = {'title': book_title, 'author': book_author}
    return BOOKS[f'book_{current_book_id + 1}']

@app.put("/{book_name}")
async def update_book(book_name: str, book_title: str, book_author: str):
    book_information = {'title': book_title, 'author':book_author}
    BOOKS[book_name] = book_information
    return book_information



@app.get("/directions/{direction_name}")
async def get_direction(direction_name: DirectionName):
    if direction_name == DirectionName.north:
        return {"Direction": direction_name, "sub": "Up"}
    if direction_name == DirectionName.west:
        return {"Direction": direction_name, "sub": "Left"}
    if direction_name == DirectionName.south:
        return {"Direction": direction_name, "sub": "Down"}
    if direction_name == DirectionName.east:
        return {"Direction": direction_name, "sub": "Right"}