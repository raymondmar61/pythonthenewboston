#newboston 56 Sorting Custom Objects
#sort custom objects by any attributes user wants

from operator import attrgetter

class User:
	def __init__(self, x, y):
		self.name = x
		self.user_id = y
	# string representation of an object.  In this case, name and user_id.
	def __repr__(self):
		return self.name + " : " + str(self.user_id)
#each item in list users is calling the class User		
users = [
	User("Bucky", 43),
	User("Sally", 5),
	User("Tuna", 61),
	User("Brian", 2),
	User("Joby", 77),
	User("Amanda", 9)
]
for user in users:
	print(user) #print Bucky : 43
# Sally : 5
# Tuna : 61
# Brian : 2
# Joby : 77
# Amanda : 9

print("-----")
for user in sorted(users,key=attrgetter("name")):
	print(user) #print Amanda : 9
# Brian : 2
# Bucky : 43
# Joby : 77
# Sally : 5
# Tuna : 61

print("-----")
for user in sorted(users,key=attrgetter("user_id")):
	print(user) #print #Amanda : 9
# Brian : 2
# Sally : 5
# Amanda : 9
# Bucky : 43
# Tuna : 61
# Joby : 77
