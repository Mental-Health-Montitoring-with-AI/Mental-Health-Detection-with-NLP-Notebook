from mentalHealth import detect_mental_health
import socket			

print("Creating Socket")
s = socket.socket()		

print ("Socket successfully created")

port = 8888			

s.bind(('', port))		
print ("socket binded to %s" %(port))

s.listen(500)	
print ("socket is listening")		

while True:

    # Establish connection with client.
    c, addr = s.accept()	

    req = c.recv(1024).decode()
    print(f"Request to detect mental health of the sentence {req} recieved from {addr} ")

    mental_health = detect_mental_health(req)
    c.send(mental_health.encode())

    print(f"Response {mental_health} sent to {addr}")

    c.close()