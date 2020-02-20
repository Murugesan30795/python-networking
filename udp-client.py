import socket 

client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host="www.google.com"
port=80

Access_key_id ='AKIAXPF5KZBAMUIISW5T'
Secret_access_key='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'

client.sendto(b'GET / HTTP/1.1\r\nHost: google.com\r\n\r\n',(host,port))

data,adds=client.recvfrom(4096)

print (data)
print 
print 
print (adds)




