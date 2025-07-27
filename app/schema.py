from pydantic import BaseModel, Field, field_validator
from typing import Literal, Annotated
from datetime import datetime

class Todovalidation(BaseModel):
    title: str = Field(..., min_length= 3, max_length= 50, description="WHAT ARE YOU PLANNING")
    description : str | None = Field(None, max_length= 200, description="YOUR DETAILED DESCRIPTION")
    completed: bool = False

@field_validator('title') 
# here cls is the class (the Pydantic model) being validated & v is the value of the title field that the user is trying to set.
def title_must_present(cls, v):
    if not v or not v.strip():
        raise ValueError('Title cannot be empty')
    return v 


class Todo(Todovalidation):
    id: int
    created_at : datetime | None=None
    updated_at : datetime | None=None

