import socket
import threading
from queue import Queue
	
Host = '10.0.0.'
Port = 5555

q = Queue()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def LANscan(ip):
	try:
		print(socket.gethostbyaddr(Host+str(ip)))
	except:
		pass

def threader():
	while True:
		worker = q.get()
		LANscan(worker)
		q.task_done()

for x in range(256):
	t = threading.Thread(target=threader)
	t.deamon = True
	t.start()
	
for worker in range(1,256):
	q.put(worker)
		
q.join()
