# Description: This is a simple UDP client program that sends a message to a server and waits for a response.

from socket import *

serverName = 'localhost'
serverPort = 12000

# Creating a UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

message = input('Input lowercase sentence:')
clientSocket.sendto(message.encode(), (serverName, serverPort))

# Receiving the modified message from the server
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())

clientSocket.close()

# Description: This is a simple UDP server program that response to a client message.

from socket import *

serverPort = 12000

# Creating a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Assigning the server port number to the server's socket
serverSocket.bind(('', serverPort))

print('The server is ready to receive')

while True:
    # Receiving the client's message and address
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)

# Path: Socket_programming_TCP.py
