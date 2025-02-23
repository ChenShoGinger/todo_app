from fastapi.testclient import TestClient
from main import *

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to TODO LIST APP"}

def test_create_todo():
    todo_data = Todo(task="Finish homework", id=1, completed=False, category="SCHOOL").model_dump()
    response = client.post("/todos", json=todo_data)
    assert response.status_code == 200

    response_json = response.json()
    assert response_json["task"] == todo_data["task"]
    assert response_json["id"] == todo_data["id"]
    assert response_json["completed"] == todo_data["completed"]
    assert response_json["category"] == todo_data["category"]
    client.delete(f"/todos/SCHOOL/1")


def test_read_todos():
    response = client.get("/todos")
    assert response.status_code == 200
    todos = response.json()
    assert isinstance(todos, list)


def test_update_todo():
    create_response = client.post(
        "/todos",
        json={"task": "Update this task", "id": 1, "completed": False, "category": "TestToUpdate"}
    )
    assert create_response.status_code == 200
    created_todo = create_response.json()

    updated_todo = {
        "task": "Updated task", #updating also task data and completed status
        "completed": True,
        "category": created_todo["category"], 
        "id": created_todo["id"]  
        }

    update_response = client.put(f"/todos/{created_todo['category']}/{created_todo['id']}", json=updated_todo)
    assert update_response.status_code == 200

    get_response = client.get("/todos")
    todos = get_response.json()
    updated_todo = next((todo for todo in todos if todo["id"] == created_todo["id"] and todo["category"] == created_todo["category"]), None)

    assert updated_todo is not None
    assert updated_todo["task"] == "Updated task"
    assert updated_todo["completed"] is True
    client.delete(f"/todos/TestToUpdate/1")


def test_delete_todo():
    create_response = client.post(
        "/todos",
        json={"task": "Delete this task", "id": 999, "completed": False, "category": "TestDelete"}
    )
    assert create_response.status_code == 200
    
    delete_response = client.delete(f"/todos/TestDelete/999")
    assert delete_response.status_code == 200
    assert delete_response.json() == {"success": "Task deleted"}

    get_response = client.get("/todos")
    todos = get_response.json()
    assert not any(todo for todo in todos if todo["id"] == 999 and todo["category"] == "TestDelete") #this task does not exist anymore
    