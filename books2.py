from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field
from uuid import UUID

app = FastAPI()


class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=12)
    author: str
    description: Optional[str] = Field(title="Description of the book", max_lengh=100, min_length=1)
    rating: int


BOOKS = []


@app.get("/")
async def read_all_books():
    return BOOKS


@app.post("/")
async def create_book(book: Book):
    BOOKS.append(book)
    return book
