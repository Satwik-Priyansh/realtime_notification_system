import socket
import threading
import requests

# Define the list of backend Flask servers
backends = ['http://127.0.0.1:5000', 'http://127.0.0.1:5001', 'http://127.0.0.1:5002']
current_backend = 0

def get_next_backend():
    global current_backend
    backend = backends[current_backend]
    current_backend = (current_backend + 1) % len(backends)
    return backend

def handle_client(client_socket):
    try:
        request = client_socket.recv(1024).decode('utf-8')
        first_line = request.split('\n')[0]
        method, path, _ = first_line.split()

        backend = get_next_backend()
        print(f"Forwarding request to {backend}")

        response = requests.request(method, backend + path)
        client_socket.sendall(f"HTTP/1.1 {response.status_code} OK\r\n".encode('utf-8'))
        client_socket.sendall(f"Content-Length: {len(response.content)}\r\n".encode('utf-8'))
        client_socket.sendall(b"\r\n")
        client_socket.sendall(response.content)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

def start_load_balancer(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Load balancer listening on {host}:{port}")

    while True:
        client_socket, _ = server_socket.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_load_balancer('127.0.0.1', 8080)
