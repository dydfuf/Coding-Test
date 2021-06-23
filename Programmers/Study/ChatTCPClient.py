#
# ChatTCPClient.py
# ver 1.0
# 20160207 KIMDOIL
#
import datetime
from socket import *
import sys
import re
from select import select

clientVersion = '1.0'

serverName = 'localhost'
serverPort = 10207

# Get nickname for chat room from argv
if len(sys.argv) < 2:
    print("Invalid Nickname. Try again")
    exit(0)
else:
    nickname = sys.argv[1]

# Invalid Nickname Exception
regex = re.compile('[a-zA-Z-]{1,32}')

if not regex.fullmatch(nickname):
    print("Invalid Nickname. Try again")
    exit(0)

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
clientSocket.settimeout(2)

flag = False

requestTime = 0

commands = ['\\list', '\\dm', '\\ex', '\\quit', '\\ver', '\\rtt']

try:
    clientSocket.connect((serverName, serverPort))
    clientSocket.send(nickname.encode())

    print(clientSocket)
except:
    print('Server that you are looking for is not opened.')
    exit(0)

try:
    while True:
        if flag:
            print("여ㅛ기들어오나?")
            break
        socket_list = [sys.stdin, clientSocket]

        read_socket, write_socket, error_socket = select(socket_list, [], [], 0)

        for sock in read_socket:
            if sock == clientSocket:
                data = sock.recv(2048).decode()
                # print(data + "///" + nickname)
                if not data:
                    print('Disconnection by Server closed')
                    flag = True
                    break
                else:
                    if data[:2] == '\\0':
                        print('Chatting room full. cannot connect')
                        flag = True
                        break

                    elif data[:2] == '\\1':
                        print('That nickname is already used by another user. cannot connect')
                        flag = True
                        break

                    elif data[:2] == '\\2':
                        print("Welcome " + nickname + " to CAU network class chat room at " + str(
                            clientSocket.getpeername()) + '. You are ' + data[2:] + ' user.')

                    elif data[:2] == '\\v':
                        print("Server Version: ", data[2:])
                        print("Client Version: ", clientVersion)

                    elif data[:2] == '\\r':
                        responseTime = datetime.datetime.now()
                        print('RTT: ' + str((responseTime - requestTime).total_seconds() * 1000) + 'ms')

                    else:
                        print(data)

            # User entered message
            else:
                message = sys.stdin.readline()

                # Special Command
                if message[0] == '\\':
                    cmd = message.split()[0]

                    if message == '\\list\n':
                        clientSocket.send('\\l'.encode())

                    elif cmd == '\\dm' or cmd == '\\ex':
                        clientSocket.send(message.encode())

                    elif message == '\\quit\n':
                        flag = True
                        print('gg~')
                        break

                    elif message == '\\ver\n':
                        clientSocket.send('\\v'.encode())

                    elif message == '\\rtt\n':
                        requestTime = datetime.datetime.now()
                        clientSocket.send('\\r'.encode())

                    else:
                        print("Invalid Command")

                # Chatting Message
                else:
                    clientSocket.send(message.split()[0].encode())
    clientSocket.close()

# Socket close when input [ctrl-C]
except KeyboardInterrupt:
    clientSocket.close()
    print('gg~')

# Connection disconnected
except ConnectionResetError:
    clientSocket.close()
    print('Disconnection by Server closed')
    exit(0)
