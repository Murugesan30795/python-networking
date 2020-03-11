import socket

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host="172.31.43.244"
#host="www.google.com"
port=9999
Access_key_id ='AKIA6GWUVBT2WX4ZOGOW'
Secret_access_key='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'

client.connect((host,port))

client.send(b'GET / HTTP/1.1\r\nHost: google.com\r\n\r\n')
#client.send(b'hii')
response=client.recv(4098)

print (response)




