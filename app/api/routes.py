from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.extensions import db
from app.models import Task

api = Blueprint("api", __name__)

#  GET TASKS
@api.route("/tasks", methods=["GET"])
@jwt_required()
def get_tasks():
    user_id = get_jwt_identity()

    tasks = Task.query.filter_by(user_id=user_id).all()

    return jsonify([
        {
            "id": t.id,
            "title": t.title,
            "description": t.description,
            "is_completed": t.is_completed
        }
        for t in tasks
    ])

#  CREATE TASK
@api.route("/tasks", methods=["POST"])
@jwt_required()
def create_task():
    user_id = get_jwt_identity()
    data = request.get_json()

    task = Task(
        title=data["title"],
        description=data.get("description"),
        user_id=user_id
    )

    db.session.add(task)
    db.session.commit()

    return jsonify({"message": "created"})

#  UPDATE TASK
@api.route("/tasks/<int:task_id>", methods=["PUT"])
@jwt_required()
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    data = request.get_json()

    task.title = data.get("title", task.title)
    task.description = data.get("description", task.description)
    task.is_completed = data.get("is_completed", task.is_completed)

    db.session.commit()

    return jsonify({"message": "updated"})

#  DELETE TASK
@api.route("/tasks/<int:task_id>", methods=["DELETE"])
@jwt_required()
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)

    db.session.delete(task)
    db.session.commit()

    return jsonify({"message": "deleted"})