import socket
import json


COMM=["UPTIME", "INFO", "HELP", "STOP"]

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 2738))



def send_uptime(y):
    data ={}
    for x in range(len(COMM)):   
        if COMM[x]==y:
            data["message"]=y
            data2 = json.dumps(data)
            client.sendall(bytes(data2,encoding="utf-8"))
            data=client.recv(1024)
            data = data.decode("utf-8")
            print(repr(data))


print('You can choose command from list. Type {} to get information about commands.'.format(COMM[2]))
z=input()
send_uptime(z)
if z=="STOP":
    client.close()


