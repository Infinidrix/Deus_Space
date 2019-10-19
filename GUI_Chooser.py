import socket


def process_request(request):
	print("Recieved:", request)
	request = list(request)
	print("This is what happens", request)
	for i in request:
		if 65 < ord(i) < 123:
			request.remove(i)
	request = str(request)
	print("New string: ", request)
	if request == "Stars":
		send_many(star_origin)
	elif request == "hello":
		send_one("hello")


HOST = '127.0.0.1'
PORT = 8008
star_origin = ["Supernova", "Collisions", "other"]
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST, PORT))
	s.listen()
	conn, addr = s.accept()
	with conn:
		print('Connected by', addr)
		while True:
			data = conn.recv(64)
			process_request(data.decode())
			if not data:
				break

def send_one(message):

	conn.sendall(message.encode())
	print("Sent:", message.encode())
	print()

def send_many(*args):
	pass
