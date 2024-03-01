# Description: This is a simple TCP client program that sends a message to a server and waits for a response.

from socket import *

serverName = 'localhost'
serverPort = 12000

# Creating a TCP socket
clientSocket = socket(AF_INET, SOCK_STREAM)

# Establishing a TCP connection between the client and the server
clientSocket.connect((serverName, serverPort))

message = input('Input lowercase sentence:')
clientSocket.send(message.encode())

# Receiving the modified message from the server
modifiedMessage = clientSocket.recv(2048)
print(modifiedMessage.decode())

clientSocket.close()

# Description: This is a simple TCP server program that response to a client message.

from socket import *

serverPort = 12000

# Creating a TCP socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# Assigning the server port number to the server's socket
serverSocket.bind(('', serverPort))

# The server is ready to receive
serverSocket.listen(1)
print('The server is ready to receive')

while True:
    # Accepting the client's connection
    connectionSocket, addr = serverSocket.accept()
    message = connectionSocket.recv(2048).decode()
    modifiedMessage = message.upper()
    connectionSocket.send(modifiedMessage.encode())
    connectionSocket.close()

# Path: Socket_programming_TCP_client.py
