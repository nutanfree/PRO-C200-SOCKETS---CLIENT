import socket
from threading import thread
nickname = input("Enter Your Nickname: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_address = '127.0.0.1'
port = 8000
client.connect((ip_address,port))
print("connected with the server")

def receive():
    while True:
        try:
            message=client.recv(1024).decode("utf-8")
            if message=="NICKNAME":
                client.send(nickname.encode("utf-8"))
            else:
                print(message)


        except:
            print("AN ERROR OCCURED !!")
            client.close()
            break


def write():

    while True:
        message = "{}:{}".format(nickname,input(""))
        client.send(message.encode("utf-8"))


    
    
receive_thread = Thread(target=receive)
receive_thread.start()
write_thread = Thread(target=write)
write_thread.start()