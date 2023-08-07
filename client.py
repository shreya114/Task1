import socket
import json
def getDataPoint(stock):
    # Replace this with your logic to get the bid and ask price for the given stock from your data source.
    bid_price = 150  # Sample bid price for demonstration purposes
    ask_price = 160  # Sample ask price for demonstration purposes

    # Compute the stock price using the formula: (bid_price + ask_price) / 2
    price = (bid_price + ask_price) / 2

    return price

def getRatio(price_a, price_b):
    # Calculate the ratio of stock price_a to stock price_b
    ratio = price_a / price_b
    return ratio
def main():
    host = 'localhost'
    port = 8888
    
    client_socket = socket.socket
    client_socket.connect((host, port))

    stocks = ["AAPL", "GOOG", "AMZN"]
    prices = {} # Dictionary to store the stock prices

    for stock in stocks:
        # Get the stock price using getDataPoint method
        price = getDataPoint(stock)

        # Store the stock price in the prices dictionary
        prices[stock] = price

        # Send the stock name to the server
        client_socket.send(stock.encode())

        # Receive the response from the server and decode it
        response = client_socket.recv(1024).decode()

        # Parse the received JSON response
        response_data = json.loads(response)
        stock_a = stock
        stock_b = response_data["stock"]
        price_b = prices[stock_b]

        # Calculate and print the ratio using the getRatio method
        ratio = getRatio(price, price_b)
        print(f"Ratio {stock_a}:{stock_b} = {ratio}")

    client_socket.close()

if __name__ == "__main__":
    main()
