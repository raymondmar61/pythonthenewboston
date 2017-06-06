class Mario():

	def move(self):
		print("I am moving!")

class Shroom():
	
	def eat_schroom(self):
		print("Now I am big!")

class BigMario(Mario, Shroom): #inherit Mario() and Shroom() functionality classes
	pass #if you need a line which you want to do nothing.  Something does nothing.

bm = BigMario()
bm.move() #BigMario() inherit move() function from Mario() class
bm.eat_schroom() #BigMario() inherit eat_schroom() function from Shroom() class