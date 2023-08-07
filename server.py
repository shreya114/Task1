import socket
import json

def handle_client(client_socket):
    stocks_data = {
        "AAPL": {"bid": 150, "price": 150},
        "GOOG": {"bid": 2700, "price": 2700},
        "AMZN": {"bid": 3500, "price": 3500}
    }

    while True:
        request = client_socket.recv(1024)
        if not request:
            break

        request_data = json.loads(request.decode())
        stock_name = request_data["stock"]

        if stock_name in stocks_data:
            response_data = {
                "stock": stock_name,
                "bid": stocks_data[stock_name]["bid"],
                "price": stocks_data[stock_name]["price"],
                "ratio": 1
            }
            response = json.dumps(response_data).encode()
            client_socket.sendall(response)

    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8888))
    server_socket.listen(1)
    print("Server listening on port 8888...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Accepted connection from {addr}")
        handle_client(client_socket)

if __name__ == "__main__":
    main()
