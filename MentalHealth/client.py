# Import socket module
import socket			

# while True:
# Create a socket object
s = socket.socket()		

# Define the port on which you want to connect
port = 8888			

# connect to the server on local computer
s.connect(('192.168.0.105', port))

# while True:

sentence = input("Enter Sentence: ")
# print(sentence.encode())
s.send(sentence.encode())
print(f"Sentence '{sentence}' sent to server through port number {port}")
print (f"Response got : {s.recv(1024).decode()}")
s.close()	

