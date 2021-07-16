import socket
import json
import time
import threading
import os

from sample_working_with_json import find_user, is_valid_password

x=os.path.abspath('server2.py')
print(x)
#nie mogę odpalać servera z cmd bo coś ze ścieżkami... i nie mogę z pliku z json-ami odczytać

class User():
    def __init__(self, name):
        self.name = name
        #czy atrybut is admin?

    def read(self,conn):
        type={"message":"Do you want read all mesages or for who?"}
        data_to_server=json.dumps(type)
        conn.send(bytes(data_to_server, encoding=UTF))
        pass #komuinikacja, że chcę od konkretnej osoby/lub wszystkie

    #def read_all():
    #    pass #komunikacja, że chcę doczytać wszystkie wiadomości

    def send(self,conn):
        pass #wysłać sygnał, że chcę wysłać komuś

    def log_out(self):
        pass

#może przenieść. porozbijać na pliki.
class Admin(User):
    def init(self, name):
        self.name = name

    def read_user():
        pass#czyta od kogo chce wiadomości

    #def read_user_all():
    #    pass#czyta wszystkie usera


#socket.gethostbyname(socket.gethostname())
IP_SERVER="127.0.0.1"
PORT=2738
UTF="utf-8"
VERSION_OF_SERVER=112

MESSAGES={"UPTIME":"TIME OF CONNECTION WITH CLIENT APPLICATION", "INFO":"SERVER VERSION NUMBER, DATE OF SERVER CREATION(???)", "HELP":{"LIST OF AVAILABLE COMMANDS":{"UPTIME":"cos", "INFO":"cos", "STOP":"cos", "LOG IN":"wez z wyzej"}}, "STOP":"SERVER DISCONNECTION", "LOG IN":"LOG IN AND GET ACCESS TO PERSONAL DATA", "READ":"READ YOUR MESSAGES, IF LOGGED IN", "SEND": "SEND MESSAGES TO OTHERS USERS, IF YOU ARE LOGGED IN", "READ_USER": "READ MESSAGES OTHERS MEMBERS. ONLY FOR ADMIN"}


server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP_SERVER, PORT))

begin=time.time()
begin2=time.ctime(begin)

print("Connection time", begin2)
print("Server IP address:", IP_SERVER)

def start():
    server.listen()
    while True:
        conn, address = server.accept()
        
        print ('Klient z adresu', address)
        
        thread=threading.Thread(target=client, args=(conn, address))
        thread.start()

def client(conn, address):
    connected=True
    while connected:
        end=time.time()
        end2=time.ctime(end)
        print("Czas połączenia z klientem: ", end2)
        data = conn.recv(1024)
        data = data.decode(UTF)
        data = json.loads(data)
        print(data)
        print(data['message'])
        
        a=data['message']
        func= {
            "INFO": info(begin2),
            "UPTIME": uptime(end, begin),
            "HELP": help(),
            "STOP": stop(),
            "LOG IN": log_in(conn)
        }
        data_to=func.get(a)
        #while data_to=log_in():
    """
        data_to_server=json.dumps(data_to)
        print(data_to)
        conn.send(bytes(data_to_server, encoding=UTF))    
        #plus handle default
    """
            
def uptime(end, begin):
    uptime_value={}
    uptime=end-begin
    MESSAGES["UPTIME"]=uptime
    return MESSAGES.fromkeys(["UPTIME"], uptime)

def info(begin2):
    info={}
    info["SERVER VERSION NUMBER"]=VERSION_OF_SERVER
    info["DATE OF SERVER CREATION"] = begin2
    MESSAGES["INFO"]=info
    return MESSAGES.fromkeys(["INFO"], info)
     
#help wysyła bez "help:"". ale chyba może być
def help():
    return MESSAGES["HELP"]["LIST OF AVAILABLE COMMANDS"]

def stop():
    return {"STOP":"SERVER DISCONNECTION"}

def log_in(conn):
    #data = conn.recv(1024)
    #data = data.decode(UTF)
    #data = json.loads(data)
    #print(data)
    type={"message":"please type your username:   "}
    data_to_server=json.dumps(type)
    conn.send(bytes(data_to_server, encoding=UTF))
    #teraz musi pobrać username od clienta
    data = conn.recv(1024)
    data = data.decode(UTF)
    data = json.loads(data)
    username = data["username"]
    x={"message":"Password"}
    y={"message":"Invalid login. Try again"}
    if find_user(username):
        data_to_server=json.dumps(x)
        conn.send(bytes(data_to_server, encoding=UTF))   
    else:
        data_to_server=json.dumps(y)
        conn.send(bytes(data_to_server, encoding=UTF)) 
    #to try again trzeba ogarnąć
    data = conn.recv(1024)
    data = data.decode(UTF)
    data = json.loads(data)
    password = data["password"]
    print(password)
    x={"message":"You are logged in!"}#plus co jak coś innego type
    y={"message": "Invalid password. Try again!"}
    if is_valid_password(username, password):
        data_to_server=json.dumps(x)
        conn.send(bytes(data_to_server, encoding=UTF))
        user=User(username)
        x={"message": " What do you want to do? READ or SEND - please type one of mentioned"}
        data_to_server=json.dumps(x)
        conn.send(bytes(data_to_server, encoding=UTF))
        data= conn.recv(1024)
        data = data.decode(UTF)
        data = json.loads(data)
        #tu przyjmuję info read lub send itd. a co jak user chce jakąś informację spoza??? powinna być mozliwość odwołania do help
        if data["message"]=="READ":
            user.read(conn)
        elif data["message"]=="SEND":
            user.send(conn)
        else:
            data={"message": "Please type again"}#czy coś tak
            data_to_server=json.dumps(data)
            conn.send(bytes(data_to_server, encoding=UTF))
    else:
        data_to_server=json.dumps(y)
        conn.send(bytes(data_to_server, encoding=UTF))
        #no i jakoś cofnąć, jak źle password wpisany
        #plus handle default


def receive_msg():
    pass

def lst_of_msg():
    pass

def logout():
    pass


if __name__=="__main__":
    start()


#na zaś - pewnie porozbijać na pliki
#testy integracyjne też do tego???

#klasa user? odczytaj komunikat i wyciagnij adekwatne dane i odeslij. gdy przyjdzie do zapisu (bo ktos wyslal) i przekroczy 5 to komunikat
#klasa admin moze ze wszystkich czytac i zmieniac haslo (chyba tez)
#zwykly user czyta tylko swoje wiadomosci i swoje danie zmienia
#odbijanie piłeczki z serwerem na poziomie klasy
