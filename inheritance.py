#getting something from someone else

class Parent(): #class beings with a uppercase letter

	def print_last_name(self):
		print("Roberts")

class Child(Parent): #type the name of the another class in paranthesis, Child() class inherit everything inside the class which is Parent(); in this case Child() has print_last_name from Parent()
	def print_first_name(self):
		print("Bucky")

	def print_last_name(self):
		print("Snitzleberg")

bucky = Child() #assign Child() class to object bucky
bucky.print_first_name() #bucky prints first name from Child()
bucky.print_last_name() #bucky prints last name from Child()'s Parent(); however Child() print_last_name overrided Parent() print_last_name