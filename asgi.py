# asgi.py
from socketio import ASGIApp

from app import app, socketio as sio

asgi_app = ASGIApp(sio, app)
