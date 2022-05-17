import socketio as sk

sio = sk.Server()
app = sk.WSGIApp(sio)

@sio.event
def connect(sid, environ):
    print(sid, 'connected')

@sio.event
def disconnect(sid):
    print(sid, 'disconnected')
