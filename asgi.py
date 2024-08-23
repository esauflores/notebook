# asgi.py
import socketio

from app import app, socketio as app_socketio

asgi_app = socketio.ASGIApp(app_socketio, app)
