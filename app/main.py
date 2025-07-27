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

@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo_by_Id(todo_id : int):

    for item in todos:
        if item['id'] == todo_id:
            return item
        
    raise HTTPException(status_code=404, detail="Todo not found")


@app.put("/todos/{todo_id}", response_model=Todo)

#below updated is the variable name we chose to change the existing Todovalidation without this it wound not now what to change and validate
def update_Todo(todo_id : int, updated: Todovalidation):
   for ids, item in enumerate(todos):
       if item['id'] == todo_id:
           todos[ids] = {
                "id": todo_id,
                "title": updated.title,
                "description": updated.description,
                "completed": updated.completed
            } 
       return todos[ids]
   raise HTTPException(status_code=404, detail="Todo not found")


@app.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int):
    for ids, item in enumerate(todos):
        if item["id"] == todo_id:
            todos.pop(ids)
            return JSONResponse(content={"message": "Todo deleted successfully"})
    raise HTTPException(status_code=404, detail="Todo not found")    



