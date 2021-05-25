import socket
import sys
import json

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'

UPTIME_MESSAGE="UPTIME"
INFO_MESSAGE = "INFO"
HELP_MESSAGE = "HELP"
DISCONNECT_MESSAGE = "STOP"
DIC={"UPTIME_MESSAGE":"UPTIME", "INFO_MESSAGE":"INFO"}
#SERVER = socket.gethostbyname(socket.gethostname())
#ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 2738))



data = json.dumps(j)
"""
    s.sendall(bytes(data,encoding="utf-8"))
    a = s.recv(1024)
    a = a.decode("utf-8")
    print ('Json: ', repr(a))
"""
def send_uptime(y):
    for x in DIC:
        if DIC[x]==y:
            data = json.dumps(x)
            client.sendall(bytes(data,encoding="utf-8"))
            data=client.recv(1024)
            data = data.decode("utf-8")
            print('JSON:', repr(data))

    
send_uptime("UPTIME")