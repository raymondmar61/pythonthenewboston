#class, simple definition, group similar variables and functions together

class Enemy: #class beings with a capital letter
	life = 3

	def attack(self): #self is a keyword, use something from its own class
		print("ouch!")
		self.life -=1 #take the life identified with "self." b/c life defined in class above subtract one"
	def checklife(self):
		if self.life <= 0:
			print("I am dead")
		else:
			print(str(self.life) + " life left")			
		pass

#need to create an object to use a class
enemy1 = Enemy() #enemy1 is an object to use class Enemy()
enemy2 = Enemy() #each object is a copy of its class, independent

enemy1.attack() #enemy1 is an object from class Enemy(), go to class Enemy and run attack()
enemy1.attack() #enemy1 is an object from class Enemy(), go to class Enemy and run attack()
enemy1.checklife()
enemy2.checklife() 