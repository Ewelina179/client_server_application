import socket
import time
import threading
import json

ip_server='127.0.0.1'
port=2738
HEADER = 64
FORMAT = 'utf-8'

UPTIME_MESSAGE="UPTIME"
INFO_MESSAGE = "INFO"
HELP_MESSAGE = "HELP"
DISCONNECT_MESSAGE = "STOP"

DIC={"message":"UPTIME", "INFO_MESSAGE":"INFO"}
#t = time.localtime()
#print "time.asctime(t): %s " % time.asctime(t)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    s.bind((ip_server, port))
    begin=time.time()
    print("Czas socketu bind: ", begin)
    print("IP_serwera:", ip_server)
    s.listen(10)
    conn, addres=s.accept()
    with conn: 
        end=time.time()
        print ('Klient z adresu', addres)
        print("Czas połączenia z klientem: ", end)
        while True:
            uptime_value={}
            uptime=end-begin
            uptime_value["Czas"]=uptime
            print(uptime_value)
            data = conn.recv(1024)
            data = data.decode("utf-8")
            data=json.loads(data)
            print(data)
            print(type(data))
            if data["message"] == "UPTIME":
                print(data)
                data2=json.dumps(uptime_value)
                #conn.send(data2)
            #if not data:
            #    break
            #elif data=="uptime":
            #    conn.send(uptime)
            conn.sendall(bytes(data2,encoding="utf-8"))
"""
while 1:
	client,addr = s.accept() # odebranie polaczenia
	print 'Polaczenie z ', addr
	client.send(time.ctime(time.time())) # wyslanie danych do klienta
	client.close()
"""