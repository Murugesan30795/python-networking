import socket
import threading

bind_ip='0.0.0.0'
bind_port=9999
Access_key_id ='AKIAXPF5KZBAMUIISW5T'
Secret_access_key='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'

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))

server.listen(5)

print "[*] Listening on %s:%d" % (bind_ip,bind_port)

def client_handler(client_socket):
	request=client_socket.recv(1024)
	print "[*] Received: %s" % request
	client_socket.send('ACK!')
	client_socket.close()

while True:
	client_sock,addr=server.accept()
	print "[*] Accepted connection from: %s:%d" % (addr[0],addr[1])
	handler=threading.Thread(target=client_handler,args=(client_sock,))
	handler.start()





