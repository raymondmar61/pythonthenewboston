#newboston 29 Classes and Objects, 30 init, 31 Class vs Instance Variables, 32 Inheritance, 33 Multiple Inheritance

#simple definition class is a way to group similar functions and variables together
#class name begins with a Uppercase letter

class Enemy29:
	life = 3
	def attack(self):
		print("ouch!")
		self.life -= 1
	def checkLife(self):
		if self.life <= 0:
			print("I am dead")
		else:
			print(str(self.life) + " life left.")
#create two objects enemy1 = Enemy() and enemy2 = Enemy() below
enemy1 = Enemy29()
enemy2 = Enemy29()
enemy1.attack() #displays ouch!
enemy1.attack() #displays ouch!
enemy1.checkLife() #displays 1 life left.
enemy2.checkLife() #displays 3 life left.

#init is a function called automatically when an object is created

class Tuna:
	def __init__(self):
		print("blrrblrlbrlbrbr")
	def swim(self):
		print("I am swimming")
flipper = Tuna()
flipper.swim() #returns blrrblrlbrlbrbr \n I am swimming.  Even though we didn't call or type flipper.__init__().  Calling Tuna class looks and calls __init__() function.

class Enemy30:
	def __init__(self, energy):
		self.energy = energy
	def get_energy(self):
		print(self.energy)
jason = Enemy30(5) #create jason object with 5 energy initializing
sandy = Enemy30(18) #create sandy object with 18 energy initializing
jason.get_energy() #returns 8
sandy.get_energy() #returns 18

class Girl:
	gender = "female"  #gender is a class variable
	def __init__(self, name):
		self.name = name #self.name is an instance variable
r = Girl("Rachel")
s = Girl("Stanky")
print(r.gender) #prints female
print(s.gender) #prints female
print(r.name) #prints Rachel
print(s.name) #prints Stanky

#inheritance simple definition is getting something from someone else

class Parent():
	def print_last_name(self):
		print("Roberts")
class Child(Parent):
	def print_first_name(self):
		print("Bucky")
	def print_last_name(self):
		print("Snitzleberg")
bucky = Child() #assign Child() class to object bucky
bucky.print_first_name() #returns Bucky
bucky.print_last_name() #returns Roberts if def print_last_name(self): in Child(Parent) wasn't written.  Child() print_last_name overrided Parent() print_last_name
bucky.print_last_name() #returns Snitzleberg

class Mario():
	def move(self):
		print("I am moving!")
class Shroom():
	def eat_shroom(self):
		print("Now I am big!")
class BigMario(Mario, Shroom): #inherit Mario() and Shroom()
	pass
bm = BigMario()
bm.move() #returns I am moving!
bm.eat_shroom() #returns Now I am big!