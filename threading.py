#threading breaks up a code to run multiple codes simultaneously

import threading

class BuckysMessenger(threading.Thread): #inherit Thread functions from threading import?
	def run(self):
		for _ in range(10): #loop ten times no need for variable use underscore
		print(threading.currentThread().getName())

#Two different threads x and y print two different names Send.. and Receive..
x = BuckysMessenger(name="Send out messages")
y = BuckysMessenger(name="Receive messages")

x.start() #create a thread call start() function goes to the class to look for run () function
y.start()