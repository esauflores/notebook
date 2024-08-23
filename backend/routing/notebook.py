# /backend/routing/notebook.py

from flask import jsonify, request
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import joinedload

from app import app, db
from backend.models import Notebook


@app.route("/api/notebooks", methods=["GET"])
def get_notebooks():
    notebooks = [notebook.to_dict() for notebook in Notebook.query.all()]
    return jsonify(notebooks)


@app.route("/api/notebook/<int:notebook_id>", methods=["GET"])
def get_notebook(notebook_id):
    notebook = Notebook.query.options(joinedload(Notebook.notes)).get_or_404(
        notebook_id
    )
    return jsonify(notebook.to_dict())


@app.route("/api/notebook/create", methods=["POST"])
def create_notebook():
    data = request.get_json()
    name = data.get("name")

    notebook = Notebook(name=name)
    db.session.add(notebook)

    try:
        db.session.commit()
        return jsonify(notebook.to_dict()), 201
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({"error": "Failed to create notebook"}), 500


@app.route("/api/notebook/delete/<int:notebook_id>", methods=["DELETE"])
def delete_notebook(notebook_id):
    notebook = Notebook.query.get_or_404(notebook_id)
    db.session.delete(notebook)

    try:
        db.session.commit()
        return jsonify(notebook.to_dict()), 200
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({"error": "Failed to delete notebook"}), 500


@app.route("/api/notebook/update/<int:notebook_id>", methods=["PUT"])
def update_notebook(notebook_id):
    notebook = Notebook.query.get_or_404(notebook_id)

    data = request.get_json()
    notebook.name = data.get("name", notebook.name)

    try:
        db.session.commit()
        return jsonify(notebook.to_dict()), 200
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({"error": "Failed to update notebook"}), 500


@app.route("/api/reset_all/doom", methods=["GET"])
def reset_all():
    db.drop_all()
    db.create_all()
    return jsonify({"message": "All tables have been reset"})
