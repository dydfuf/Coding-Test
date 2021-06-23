#
# ChatTCPServer.py
# ver 1.0
# 20160207 KIMDOIL
#
import errno
from select import select
from socket import *
import time

def send_to_all(sock, message):
    # Message not forwarded to server and sender itself
    for socket in connection_list:
        if socket != serverSocket and socket != sock:
            try:
                socket.send(message.encode())
            except Exception as e:
                print(e)
                # if connection not available
                socket.close()
                connection_list.remove(socket)


if __name__ == "__main__":

    try:
        # Software version of server & client
        serverVersion = '1.0'

        # Create server socket
        serverPort = 10207
        serverSocket = socket(AF_INET, SOCK_STREAM)

        # Option to restart server socket after existing
        serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

        serverSocket.bind(('', serverPort))
        serverSocket.listen(1)

        # List for sockets that wait connection
        connection_list = [serverSocket]

        # Start time of server
        startTime = time.time()

        # Dictionary for mapping client Nickname and <ip, port>
        clientNicknameDict = {}
        idVal = 0
        print("The server is ready to receive on port", serverPort)

        while connection_list:
            # Select function declare
            read_socket, write_socket, error_socket = select(connection_list, [], [], 0)

            for sock in read_socket:
                # Occur new connection
                if sock == serverSocket:
                    (connectionSocket, clientAddress) = serverSocket.accept()

                    name = connectionSocket.recv(4096).decode()
                    print(len(connection_list))
                    if len(connection_list) > 2:
                        connectionSocket.send('\\0'.encode())
                        # connection_list.remove(connectionSocket)
                    else:
                        # Repeated name exception
                        if name in clientNicknameDict.values():
                            connectionSocket.send('\\1'.encode())
                            # connection_list.remove(connectionSocket)
                        else:
                            connectionSocket.send(('\\2' + str(len(connection_list))).encode())
                            connection_list.append(connectionSocket)
                            clientNicknameDict[connectionSocket] = name
                            print(clientNicknameDict.values())
                            print(clientNicknameDict[connectionSocket] + ' joined. There are ' + str(
                                            len(connection_list) - 1) + ' users connected.')
                            send_to_all(connectionSocket,
                                        clientNicknameDict[connectionSocket] + ' joined. There are ' + str(
                                            len(connection_list) - 1) + ' users connected.')

                # Receive message from connected socket
                else:
                    try:
                        message = sock.recv(2048).decode()

                        # Case of client socket closed
                        if not message:
                            connection_list.remove(sock)
                            print(clientNicknameDict[sock.getpeername()] + ' left. There are ' + str(
                                len(connection_list) - 1) + ' users now.')
                            send_to_all(sock, clientNicknameDict[sock] + ' left. There are ' + str(
                                len(connection_list) - 1) + ' users now.')
                            clientNicknameDict.pop(sock)
                            sock.close()
                            break
                        else:
                            if message == '\\l':
                                msg = ''
                                for client in connection_list:
                                    if client != serverSocket:
                                        clientAddr = client.getpeername()
                                        msg += '<{}, {}, {}>\n'.format(clientNicknameDict[client], clientAddr[0], clientAddr[1])
                                sock.send(msg.encode())

                            elif message.split()[0] == '\\dm':
                                print(message)
                                # keys = clientNicknameDict.keys()
                                # for key in keys:
                                #     if clientNicknameDict[key] ==

                                # for client in connection_list:
                                #     if client != serverSocket:
                                #         print(clientNicknameDict[client])
                                #         if message.split()[1] == clientNicknameDict[client]:
                                #             print(message.split())
                                #             print(client)
                                #             print(sock)
                                #             sock.send("dm sent".encode())
                                #             client.send(('from: ' + clientNicknameDict[sock] + message.split()[2]).decode())
                                #             break

                            elif message.split()[0] == '\\ex':
                                print("exexexexeex")
                                for client in connection_list:
                                    if client != serverSocket:
                                        if message.split()[1] == clientNicknameDict[client]:
                                            continue
                                        else:
                                            client.send(message.split()[2].decode())

                            elif message == '\\v':
                                sock.send(('\\v' + serverVersion).encode())

                            elif message == '\\r':
                                sock.send(message.encode())

                            elif "i hate professor" in message:
                                connection_list.remove(sock)
                                print(clientNicknameDict[sock] + ' left. There are ' + str(
                                    len(connection_list) - 1) + ' users now.')
                                send_to_all(sock, clientNicknameDict[sock] + ' left. There are ' + str(
                                    len(connection_list) - 1) + ' users now.')
                                clientNicknameDict.pop(sock)
                                sock.close()
                            else:
                                send_to_all(sock, clientNicknameDict[sock] + ': ' + message)

                    except:
                        connection_list.remove(sock)
                        print(clientNicknameDict[sock] + ' left. There are ' + str(
                            len(connection_list) - 1) + ' users now.')
                        send_to_all(sock, clientNicknameDict[sock] + ' left. There are ' + str(
                            len(connection_list) - 1) + ' users now.')
                        clientNicknameDict.pop(sock)
                        sock.close()

    # Close socket when input [ctrl-C]
    except KeyboardInterrupt:
        serverSocket.close()
        print('Bye bye~')
