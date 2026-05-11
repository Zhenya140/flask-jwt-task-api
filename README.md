# Flask JWT Task API

REST API for task management built with Python and Flask.

## Features

- User registration
- User login
- JWT authentication
- Create task
- Read tasks
- Update task
- Delete task
- PostgreSQL database

## Tech Stack

- Python
- Flask
- Flask-JWT-Extended
- SQLAlchemy
- PostgreSQL
- Blueprint

## Project Structure

app/
├── auth/
├── api/
├── models.py
├── extensions.py
├── __init__.py

## Installation

pip install -r requirements.txt

## Run

python run.py

## API Endpoints

POST /auth/register  
POST /auth/login  

GET /api/tasks  
POST /api/tasks  
PUT /api/tasks/<id>  
DELETE /api/tasks/<id>