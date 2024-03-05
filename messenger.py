import threading
import socket
print("********************************************IMPORTANT!********************************************")
print("Developed By Aditya Srivastav!")
print("INSTRUCTIONS TO USE The Messenger")
print("1. Enter The Server Address (refer to server.exe for instructions to get server address)")
print("2. Enter Port Number (refer to server.exe for instructions on how to get the port number)")
print("3. Enter an alias name (nickname) and connect to the server and start chatting")
print("********************************************START BELOW********************************************")

server_address = str(input("Enter a Server Address: "))
port_number = int(input("Enter Port Number: "))
alias = input('Enter a Nickname >>> ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_address, port_number))


def client_receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "alias?":
                client.send(alias.encode('utf-8'))
            else:
                print(message)
        except:
            print('Error!')
            client.close()
            break


def client_send():
    while True:
        message = f'{alias}: {input("")}'
        client.send(message.encode('utf-8'))


receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()
