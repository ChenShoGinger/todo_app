# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from mongodb import create_todo, get_todos, update_todo, delete_todo


app = FastAPI()

#components of a TODO
class Todo(BaseModel):
    task: str
    id: int
    completed: bool = False
    category: str

@app.get("/")
async def root():
    return {"message": "Welcome to TODO LIST APP"}

@app.get("/todos", response_model=List[Todo])
def read_todos():
    todos = get_todos()
    return todos

@app.post("/todos", response_model=Todo)
def create_todo_item(todo: Todo):
    created_todo = create_todo(todo.model_dump())
    return created_todo


@app.put("/todos/{category}/{task_id}", response_model=Todo)
def update_todo_item(category: str, task_id: int, todo: Todo):
    if not update_todo(category, task_id, todo.model_dump()):
        raise HTTPException(status_code=404, detail="Task not found")
    return todo

@app.put("/todos/complete/{category}/{task_id}")
def complete_todo_item(category: str, task_id: int):
    if not update_todo(category, task_id, {"completed": True}):
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task completed"}

@app.delete("/todos/{category}/{task_id}")
def delete_todo_item(category: str, task_id: int):
    if not delete_todo(category, task_id):
        raise HTTPException(status_code=404, detail="Task not found")
    return {"success": "Task deleted"}


