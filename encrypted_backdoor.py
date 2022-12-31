import socket
import ssl

# Create a socket object
s = socket.socket()

# Bind the socket to a port
s.bind(("localhost", 8080))

# Listen for incoming connections
s.listen(1)

# Accept an incoming connection
conn, addr = s.accept()

# Wrap the connection in an SSL context
ssl_conn = ssl.wrap_socket(conn,
certfile="server.crt",
keyfile="server.key",
ssl_version=ssl.PROTOCOL_TLSv1)

# Send data to the connection
ssl_conn.send("Hello, world!")

# Receive data from the connection
data = ssl_conn.recv(1024)
print(data)

# Close the connection
ssl_conn.close()
