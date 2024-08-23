# /backend/models/notebook.py


from sqlalchemy import func, select
from sqlalchemy.orm import column_property

from app import db
from backend.models.note import Note


class Notebook(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    notes = db.relationship("Note", backref="notebook", cascade="all, delete-orphan")
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    notes_count = column_property(
        select(func.count(Note.id)).where(Note.notebook_id == id).scalar_subquery(),
    )

    def __repr__(self):
        return f"<Notebook {self.name}>"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "notes_count": self.notes_count,
            "notes": [note.to_dict() for note in self.notes],
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
