from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field
from uuid import UUID

app = FastAPI()


class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=12)
    author: str = Field(min_length=1, max_length=100)
    description: Optional[str] = Field(title="Description of the book", max_lengh=100, min_length=1)
    rating: int = Field(gt=-1, lt=101)


BOOKS = []


@app.get("/")
async def read_all_books():
    if len(BOOKS) < 1:
        create_books_no_api()
    return BOOKS


@app.post("/")
async def create_book(book: Book):
    BOOKS.append(book)
    return book


def create_books_no_api():
    book_1 = Book(id="3fa85f64-5717-4562-b3fc-2c963f66afa6", title="title 1, has to be at least 12", author="author",
                  description="description", rating=50)
    BOOKS.append(book_1);
