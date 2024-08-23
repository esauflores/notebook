# asgi.py
import socketio
from asgiref.wsgi import WsgiToAsgi

from app import app, socketio as app_socketio

asgi = WsgiToAsgi(app)

asgi_app = socketio.ASGIApp(app_socketio, asgi)
