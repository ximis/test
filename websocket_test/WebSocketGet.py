from Common.WebSocketConnect import WebSocketConnnect
from .BulletOpenApi import BulletOpenApi


def get_private_websocket():
    wss, token = BulletOpenApi().get_private_token()
    ws = WebSocketConnnect()
    ws.connect(wss, token)
    return ws


def get_public_websocket():
    wss, token = BulletOpenApi().get_public_token()
    ws = WebSocketConnnect()
    ws.connect(wss, token)
    return ws
