#newboston 34 threading

#threading breaks up a code to run multiple codes simultaneously
#threading.py invalid name.  Added tutorial to file name.
#Bucky says not good for everything because objects running together may cause errors

import threading

class BuckysMessenger(threading.Thread): #inherit Thread functions from threading import?
	def run(self):
		for _ in range(10): #loop ten times with range(10).  No need for variable for x in . . . .  Use underscore.
			print(threading.currentThread().getName())

#Two different objects x and y print two different names Send.. and Receive... running together
x = BuckysMessenger(name="Send out messages")
y = BuckysMessenger(name="Receive messages")

x.start() #prints Send out messages 10 times in no particular order.  Create a thread call start() function goes to the class to look for run () function.  Don't type x.run().
y.start() #prints Receive messages 10 times in no particular order.  Create a thread call start() function goes to the class to look for run () function.  Don't type y.run().
#With threading, you don't need to wait for x.start() to finish before y.start().  Python threading, run x.start() as soon as x.start() ends, begin y.start().  Eventually, for a brief period of time x.start() and y.start() run at the same time.