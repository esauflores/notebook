# app.py
import os

from dotenv import load_dotenv
from flask import Flask
from flask_session import Session
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    static_folder=os.path.join(BASE_DIR, "frontend", "static"),
    template_folder=os.path.join(BASE_DIR, "frontend", "templates"),
)

# Secret key
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

# Session
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_FILE_DIR"] = os.path.join(BASE_DIR, "sessions")

# SqlAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

Session(app)
db = SQLAlchemy()
db.init_app(app)
socketio = SocketIO(app, async_mode="eventlet")


# backend
from backend import *

# create database
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    socketio.run(app, debug=os.getenv("DEBUG", False))
