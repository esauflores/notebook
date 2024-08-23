# /backend/routing/note.py


from flask import jsonify, request
from sqlalchemy.exc import SQLAlchemyError

from app import app, db
from backend.models import Note


@app.route("/api/notes", methods=["GET"])
def get_notes():
    return jsonify(Note.query.all())


@app.route("/api/note/<int:note_id>", methods=["GET"])
def get_note(note_id):
    note = Note.query.get_or_404(note_id)
    return jsonify(note)


@app.route("/api/note/create", methods=["POST"])
def create_note():
    data = request.get_json()
    title = data.get("title")
    content = data.get("content", "")
    notebook_id = data.get("notebook_id")

    note = Note(title=title, content=content, notebook_id=notebook_id)
    db.session.add(note)

    try:
        db.session.commit()
        return jsonify(note.to_dict()), 201
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({"error": "Failed to create notebook"}), 500


@app.route("/api/note/delete/<int:note_id>", methods=["DELETE"])
def delete_note(note_id):
    note = Note.query.get_or_404(note_id)
    db.session.delete(note)

    try:
        db.session.commit()
        return jsonify(note.to_dict()), 200
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({"error": "Failed to delete note"}), 500


@app.route("/api/note/update/<int:note_id>", methods=["PUT"])
def update_note(note_id):
    note = Note.query.get_or_404(note_id)

    data = request.get_json()
    note.title = data.get("title", note.title)
    note.content = data.get("content", note.content)
    note.notebook_id = data.get("notebook_id", note.notebook_id)

    try:
        db.session.commit()
        return jsonify(note.to_dict()), 200
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({"error": "Failed to update note"}), 500
