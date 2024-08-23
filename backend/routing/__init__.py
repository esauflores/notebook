# /backend/routing/__init__.py

from flask import render_template

from app import app
from backend.models.notebook import Notebook


@app.route("/")
@app.route("/index")
def index():
    notebooks = Notebook.query.order_by(Notebook.created_at.desc()).all()
    notebooks = [notebook.to_dict() for notebook in notebooks]
    return render_template("index.html", notebooks=notebooks)


from backend.routing.note import *
from backend.routing.notebook import *
