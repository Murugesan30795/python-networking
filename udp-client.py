import socket 

client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host="www.google.com"
port=80

client.sendto(b'GET / HTTP/1.1\r\nHost: google.com\r\n\r\n',(host,port))

data,adds=client.recvfrom(4096)

print (data)
print 
print 
print (adds)




