#newboston 30 init, 31 Class vs Instance Variables

#init is a function called automatically when an object is created

class Tuna:
	def __init__(self):
		print("blrrblrlbrlbrbr")
	def swim(self):
		print("I am swimming")
flipper = Tuna()
flipper.swim() #prints blrrblrlbrlbrbr \n I am swimming.  Even though we didn't call or type flipper.__init__().  Calling Tuna class looks and calls __init__() function.

class Enemy:
	def __init__(self, energy):
		self.energy = energy
	def get_energy(self):
		print(self.energy)
jason = Enemy(5) #create jason object with 5 energy initializing
sandy = Enemy(18) #create sandy object with 18 energy initializing
jason.get_energy() #prints 8
sandy.get_energy() #prints 18

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