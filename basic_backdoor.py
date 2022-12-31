import socket

# Create a socket object
s = socket.socket()

# Bind the socket to a port
s.bind(("localhost", 8080))

# Listen for incoming connections
s.listen(1)

# Accept an incoming connection
conn, addr = s.accept()

# Send data to the connection
conn.send("Hello, world!")

# Receive data from the connection
data = conn.recv(1024)
print(data)

# Close the connection
conn.close()
