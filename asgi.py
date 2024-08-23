# asgi.py
from asgiref.wsgi import WsgiToAsgi
from socketio import ASGIApp

from app import app, socketio as sio

asgi_app = WsgiToAsgi(app)
asgi_app = ASGIApp(sio, app)
