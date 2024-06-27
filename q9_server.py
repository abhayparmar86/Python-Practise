import socket
import threading

def handle_client(conn, address):
    print("Connected to:", address)
    try:
        while True:
            data = conn.recv(1024).decode()
            if data.lower().strip() == 'bye':
                print("Connection with", address, "closed.")
                conn.send('Server disconnected'.encode())
                break
            else:
                print("From connected user:", address, data)
            
            response = input(' -> ')
            if response.lower().strip() == 'bye':
                conn.send(response.encode())
                print("Connection with", address, "closed.")
                break
            else:
                conn.send(response.encode())
    finally:
        conn.close() 
        print(address, "disconnected")

def server_program():
    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(5)
    print("Server is listening...")

    try:
        while True:
            conn, address = server_socket.accept()
            client_thread = threading.Thread(target=handle_client, args=(conn, address))
            client_thread.start()
    except KeyboardInterrupt:
        print("Server is shutting down...")
        server_socket.close()
    

if __name__ == '__main__':
    server_program()


# -------------------------------------------

# import socket
# import threading

# def handle_client(conn, address):
#     print("Connected to:", address)
#     while True:
#         data = conn.recv(1024).decode()
#         if data.lower().strip() == 'bye':
#             print("Connection with", address, "closed.")
#             conn.close()
#             break
#         else:
#             print("From connected user:", address, data)
        
#         response = input(' -> ')
#         if response.lower().strip() == 'bye':
#             conn.send(response.encode())
#             print("Connection with", address, "closed.")
#             conn.close()
#             break
#         else:
#             conn.send(response.encode())

# def server_program():
#     host = socket.gethostname()
#     port = 5000

#     server_socket = socket.socket()
#     server_socket.bind((host, port))

#     server_socket.listen(5)
#     print("Server is listening...")

#     try:
#         while True:
#             conn, address = server_socket.accept()
#             client_thread = threading.Thread(target=handle_client, args=(conn, address))
#             client_thread.start()
#     except KeyboardInterrupt:
#         print("Server is shutting down...")
#         server_socket.close()
    

# if __name__ == '__main__':
#     server_program()


# --------------------------------------------------------------------

# import socket
# import threading

# IP = socket.gethostbyname(socket.gethostname())
# PORT = 55555
# ADDR = (IP, PORT)
# SIZE = 1024
# FORMAT = "utf-8"
# DISCONNECT_MSG = "disconnect"

# def handle_client(conn, addr):
#     print(f"New Connection {addr} connected")
#     connected = True
#     while connected:
#         msg = conn.recv(SIZE).decode(FORMAT)
#         if msg == DISCONNECT_MSG:
#             connected = False
            
#         print(f"{addr} : {msg}")
#         msg = f"Msg Received {msg}"
#         conn.send(msg.encode(FORMAT))

#     conn.close()


# def main():
#     print("Server is Starting...")
#     server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server.bind(ADDR)
#     server.listen()
#     print(f"Server is Listening to {IP}:{PORT}")

#     while True:
#         conn, addr = server.accept()
#         thread = threading.Thread(target = handle_client, args = (conn, addr))
#         thread.start()
#         print(f"[Active Connections] {threading.active_count() - 1}")



# if __name__ == "__main__":
#     main()