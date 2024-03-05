'Chat Room Connection - Client-To-Client'

import threading
import socket

print("****************************************************************IMPORTANT!****************************************************************")
print("Developed By Aditya Srivastav")
print("1. This is the server of the chatting application")
print("2. To use this you must go to ngrok.com and download the executable")
print("3. After downloading the executable refer to a documentation or a YouTube Video on how to start a tcp connection in the ngrok console")
print("4. The usual command is 'ngrok tcp 4242' NOTE! that the port number should always be 4242")
print("5. Once the ngrok console starts running hit enter below and the server will start running successfully")
print("6. The server address and port number can be found next to 'Forwarding' in the ngrok console")
print("7. (tcp://7.tcp.eu.ngrok.io:10970) in this address the server address is (7.tcp.eu.ngrok.io) and the port number is (10790)")
print("8. Note that the server addresses and port number for each individual will be different")
print("****************************************************************START BELOW****************************************************************")

choice = str(input("If the Ngrok console up and running hit enter and the main server will start running: "))
if choice == 'y' or 'Y':

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 4242))
    server.listen()
    clients = []
    aliases = []


    def broadcast(message):
        for client in clients:
            client.send(message)

    # Function to handle clients'connections


    def handle_client(client):
        while True:
            try:
                message = client.recv(1024)
                broadcast(message)
            except:
                index = clients.index(client)
                clients.remove(client)
                client.close()
                alias = aliases[index]
                broadcast(f'{alias} has left the chat room!'.encode('utf-8'))
                aliases.remove(alias)
                break
    # Main function to receive the clients connection


    def receive():
        while True:
            print('Server is running and listening ...')
            client, address = server.accept()
            print(f'connection is established with {str(address)}')
            client.send('alias?'.encode('utf-8'))
            alias = client.recv(1024)
            aliases.append(alias)
            clients.append(client)
            print(f'The alias of this client is {alias}'.encode('utf-8'))
            broadcast(f'{alias} has connected to the chat room'.encode('utf-8'))
            client.send('you are now connected!'.encode('utf-8'))
            thread = threading.Thread(target=handle_client, args=(client,))
            thread.start()


    if __name__ == "__main__":
        receive()

