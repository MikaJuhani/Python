import socket
import copy

BUFFER_SIZE = 2048
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "www.example.com"
s.connect((host, 80))
s.send("GET / HTTP/1.1\r\nHost: " + host + "\r\n\r\n")
data = s.recv(BUFFER_SIZE)
s.close()

rawtext_array = []
for line in data:
    rawtext_array.append(line)

indexNumber = rawtext_array.index("<")
#print indexNumber
newIndex = indexNumber 

#newIndex = 321

for y in range(newIndex, len(rawtext_array)):
    print rawtext_array[y],
