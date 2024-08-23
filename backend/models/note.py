# /backend/models/note.py

from sqlalchemy import func

from app import db


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    notebook_id = db.Column(
        db.Integer, db.ForeignKey("notebook.id", ondelete="CASCADE"), nullable=False
    )

    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"<Note {self.title}>"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "notebook_id": self.notebook_id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
