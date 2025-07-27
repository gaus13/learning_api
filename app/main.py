from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from .schema import Todovalidation, Todo
from typing import List   #If you want to return a list of Todo models

app =FastAPI()

todos = []  # This is your in-memory "database" list

@app.post("/todos/")
def create_todo( todo: Todovalidation):
 # Make a new todo with an id and the info from the user(validates from pydantic model)

    global todos
    new_todo = {
        "id": len(todos) + 1,   # make a new id
        "title": todo.title,
        "description": todo.description,
        "completed": todo.completed

    }

    todos.append(new_todo)   # add to the list
    return new_todo   # show the new todo

# another way of writing the above code
# @app.post("/todos/", response_model=todo, status_code=status.HTTP_201_CREATED)
# def create_todo(todo: TodoValidation):
#     global next_id
#     new_todo = todo(id=next_id, **todo.dict())
#     todo.append(new_todo)
#     next_id += 1
#     return new_todo

@app.get("/todos/", response_model=List[Todo])
# you can add a response model: to get list of all the todo
def get_all_todo():
    return todos

@app.get("/todos/{todo_id}")