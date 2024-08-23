# asgi.py
from app import app, socketio

# Create an ASGI application using SocketIO's ASGI support
asgi_app = socketio.ASGIApp(app, socketio)
