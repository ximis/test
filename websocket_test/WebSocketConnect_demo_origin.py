from websocket import create_connection
import time
import json
import base64
import hmac
import hashlib
import requests


class WebSocketConnnect:
    def __init__(self):
        self.ws = None
        self.timeout = 4
        self.current = time.time()

    def connect(self):
        # data: [token, ws://xxx]
        token, wss = getPrivateToken()
        # testurl = "wss://push-websocket.kucoin.net/endpoint?token=%s&[connectId=welcome]" % token
        testurl = "%s?token=%s&[connectId=welcome]" % (wss, token)
        print(testurl)
        self.ws = create_connection(testurl)
        result = self.ws.recv()

        print("Received '%s'" % result)

    def close(self):
        self.ws.close()

    def subscribe(self, topic, prvateChannel=False):
        data = {
            "id": getTimeStr(),
            "type": "subscribe",
            "topic": topic,
            "response": True
        }
        if prvateChannel:
            data["privateChannel"] = True

        t = json.dumps(data)
        print("data:", data)
        self.ws.send(t)
        result = self.ws.recv()
        print("Received '%s'" % result)

    def getData(self):
        print("start -----")
        result = None

        result = self.ws.recv()
        print(time.time(), "Received '%s'" % json.dumps(json.loads(result), indent=4, separators=(',', ":")))

        return json.loads(result)

    def get_data_with_status(self, status):
        data = self.getData()
        while data['data']['status'] != status:
            data = self.getData()

        return data

    def get_data_with_subject(self, subject):
        data = self.getData()
        while data['subject'] != subject:
            data = self.getData()

        return data


def getTimeStr():
    return str((int)(time.time() * 1000))


def getPrivateToken():
    # use the account test+24@kucoin.com  k8s环境
    API_KEY = "5ee72035b3594b0009470524"
    API_SECRET = "efebbf96-266b-4736-a067-f28575d62ce5"
    API_PASSPHRASE = "a123456"

    # # use the account test+25@kucoin.com  性能环境
    # API_KEY = "5ee86629bf6fc636eb64d01c"
    # API_SECRET = "c2ce7289-0fe4-4644-b3e0-d23c3142f2b9"
    # API_PASSPHRASE = "a123456"

    open_api_host = "http://openapi-v2.kucoin.net"

    # use the account joy.test.su@gmail.com  sanbox
    # API_KEY = "5efd546797f66d0006f79b6e"
    # API_SECRET = "60fd65e4-0207-4c66-8568-914db2180c3e"
    # API_PASSPHRASE = "a123456"
    # open_api_host = "https://openapi-sandbox.kucoin.com"

    path = "/api/v1/bullet-private"
    now = int(time.time() * 1000)
    str_to_sign = str(now) + 'POST' + path
    signature = base64.b64encode(
        hmac.new(API_SECRET.encode('utf-8'), str_to_sign.encode('utf-8'), hashlib.sha256).digest())
    headers = {
        "KC-API-SIGN": signature,
        "KC-API-TIMESTAMP": str(now),
        "KC-API-KEY": API_KEY,
        "KC-API-PASSPHRASE": API_PASSPHRASE
    }
    response = requests.request('post', open_api_host + path, headers=headers)
    print(response.status_code)
    print(response.json())
    return response.json()['data']['token'], response.json()['data']['instanceServers'][0]['endpoint']


getPrivateToken()
#
# ws = WebSocketConnnect()
# ws.connect()
# ws.subscribe("/spotMarket/tradeOrders", True)
#
# ws.getData()
