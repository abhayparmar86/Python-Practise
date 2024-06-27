import socket

def client_program():
    host = socket.gethostname()  # as both code is running on the same PC
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    try:
        while True:
            message = input(" -> ")  # take input

            if message.lower().strip() == 'bye':
                client_socket.send(message.encode())
                print("Connection closed!")
                break

            client_socket.send(message.encode())  # send message
            data = client_socket.recv(1024).decode()  # receive response

            if data.lower().strip() == 'bye':
                print("Server Disconnected!")
                break
            else:
                # print("From connected user:", address, data
                print('Received from server: ' + data)  # show in terminal

    except KeyboardInterrupt:
        pass

    finally:
        client_socket.close()  # close the connection

if __name__ == '__main__':
    client_program()



# -----------------------------------------------------------------------

# import socket

# IP = socket.gethostbyname(socket.gethostname())
# PORT = 55555
# ADDR = (IP, PORT)
# SIZE = 1024
# FORMAT = "utf-8"
# DISCONNECT_MSG = "disconnect"

# c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # no need to bind direct connect
# # mention ip and port no
# c.connect(ADDR)

# while True:
#     message = input("Enter your message")
#     c.send(bytes(message, FORMAT))

# print(c.recv(1024).decode(FORMAT))