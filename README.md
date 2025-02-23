# To-Do List Application Overview📋!

This project is a simple To-Do List app designed for daily use, utilizing FastAPI and MongoDB for the backend, Streamlit for the frontend and Docker for containerization.
It allows users to manage their tasks with ease and simplicity :)

## Key Features:
- Create new tasks
- View existing tasks
- Update task details
- Delete tasks
- Mark tasks as completed

### Prerequisites:
- Docker

## Project Structure:
### Backend:
 - main.py
 - mongodb.py

Contains the FastAPI backend code (main.py) for managing to-do items using CRUD operations and interacting with MongoDB (mongodb.py) for storage.


### Frontend (ui.py):
Includes the Streamlit frontend code for the user interface, allowing users to interact with the app easily.

### docker-compose.yml:
Defines the configuration of the services, including backend, frontend, and MongoDB, enabling them to run together through Docker Compose.

## Installation Instructions⚙️:
1) **Clone the repository**:
```bash
git clone https://github.com/ChenShoGinger/todo_app.git
```

```bash
cd todolist-app
```

2) **Build the Docker containers**:
```bash
docker-compose up -d --build
```

3) **Check the status of the containers**:
```bash
docker-compose ps -a
```

## Accessing the App🔓:
** Open your browser and visit:**
http://localhost:8501 to access the To-Do list interface powered by Streamlit.

## Access App Components📱:
- **Frontend: [http://localhost:8501](http://localhost:8501/#9efe132)
- **Backend API Documentation: http://localhost:8000/docs


## Running Tests🧪:
The project includes a test script (test.py) located in the backend folder to validate the functionality of the backend API.

### Run Tests with Docker Compose:
```bash
docker exec -it <container_name_or_id> pytest /backend/test.py
```


Demo 🎥:
Check out the demo:

