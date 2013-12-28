#!/usr/bin/env python2
 

import sys, socket

class mysocket:

	def __init__(self,ip = None ,port = None, sock=None,timeout=0.1):
		if sock is None:
			self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		else:
			self.sock = sock
		self.sock.settimeout(timeout)
		self.connection = False
		if type(ip) == str and type(port) == int:
			self.connection = self.connect(ip,port)
		
	def connect(self, host, port):
		try:
			self.sock.connect((host, port))
			return True
		except:
			return False

	def send(self, msg = "", n = None):
		if type(n) == int:
			msg = msg[:n]
		try :
			if self.sock.send(msg) == 0:
				return False
			return True
		except:
			return False
		
	def receive(self):
		msg = ""
		c = self.get_one_char()
		while (c != "\n") \
		and (c != False):
			msg = msg + c
			c = self.get_one_char()
		if msg == "":
			return False
		return msg

	def get_data(self):
		msg = ""
		tm = self.receive()
		while tm :
			msg = msg + tm + "\n" 
			tm = self.receive()
		if msg == "":
			return False
		return msg
		
	def get_one_char(self):
		try:
			c = self.sock.recv(1)
		except:
			c = False
		return c
	
	def comunicate(self,msg=None):
		try:
			if type(msg) == str:
				connection.send(msg+"\n")
			return connection.get_data()
		except:
			return False

def nums_only(string):
	nstr = ""
	for c in string:
		for n in "0123456789":
			if n == c:
				nstr = nstr + n
				break
	return nstr

def extract_numbers(string):
	t = string.split(" ")
	if t[0] != "Nope,":
		return False
	sys.stdout.flush()
	return nums_only(t[8])



if __name__ == "__main__":

	try:
		connection = mysocket(sys.argv[1],int(sys.argv[2]))
	except:	
		connection = mysocket('127.0.0.1',8888)
		
	if connection.connection:
		#print "timeout : '" + str(connection.sock.gettimeout()) + "'"
		#print connection.comunicate()
		connection.comunicate()
		while True:
			rep = connection.comunicate("")
			if rep == False:
				print "error comunicating"
				break
			print extract_numbers(connection.comunicate("")) 
	else:
		print "no connection, start server first" 
