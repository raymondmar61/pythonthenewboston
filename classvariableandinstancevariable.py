class Girl:

	gender = "female" #class variable, shared with each object or girl

	def __init__(self, name):
		self.name = name  #instance variable, unique to each object or girl

r = Girl("Rachel")
s = Girl("Stanky")
print(r.gender)
print(s.gender)
print(r.name)
print(s.name)