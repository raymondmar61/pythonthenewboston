#The New Boston 2 Numbers, 3 Strings, 4 Slicing up Strings, 5 Lists, 7 if elif else, 8 for, 9 Range and While, 

"""
print(18/3.4) #print 5.294117647058823
print(18//3.4) #print 5.0
print(18/4) #print 4.5
print(18//4) #print 4
print(18/4.1) #print 4.390243902439025
print(18//4.1) #print 4.0
print(18/4.4) #print 4.090909090909091
print(18//4.4) #print 4.0
"""
print(18/5) #print 3.6
print(18//5) #print 3
print(18//5.0) #print 3.0
print(18/8) #print 2.25
print(18//8) #print 2
print(r"this story is \nokday d'kay") #print this story is \nokday d'kay
user = "Tuna McFish"
print(user[0]) #print T
print(user[1:4]) #print una
print(user[1:9:2]) #print uaMF
print(user[-1]) #print h
print(user[-1::-1]) #print hsiFcM anuT
players = [29, 58, 66, 71, 87]
print(players[2]) #print 66
players[2] = 68
print(players[2]) #print 68
newplayers = players + [90, 91, 98]
newplayers.append(120)
print(newplayers) #print [29, 58, 68, 71, 87, 90, 91, 98, 120]
newplayers[6:] = [-1, -2, -3]
print(newplayers) #print [29, 58, 68, 71, 87, 90, -1, -2, -3]
newplayers[5:] = []
print(newplayers) #print [29, 58, 68, 71, 87]
name = "Bucky"
if name is "Bucky":
	print("Hey there Bucky")
if "uck" in name:
	print("Hey there uck")
players = [29, 58, 66, 71, 87]
for eachplayers in players[0:3]:
	print(eachplayers) #print 29\n 58\n 66
for eachnumber in range(100,-51,-25):
	print(eachnumber,end=", ") #print 100, 75, 50, 25, 0, -25, -50,
print("\n")

def functionname(number=17):
	return number+50
print(functionname(150)) #print 200
print(functionname()) #print 67
def functionname2(name="Raymond",action="jump", braincells=50000000, item="glue"):
	print(name+" "+action+" "+item,braincells)
functionname2(action="run") #print Raymond run glue 50000000
functionname2(action="sleep", braincells=100000000) #print Raymond sleep glue 100000000
def addnumbers(*numbers,ray="sunshine"):
	total = 0
	for a in numbers:
		total += a
	print(total)
	print(ray)
addnumbers(3, 32) #print 35\n sunshine
addnumbers(-30, 30, 32, ray="moon") #print 32\n moon
players = [29, 58, 66, 71, 87]
addnumbers(*players) #print 311\n sunshine
print("\n")

groceryset = {"cereal","milk","starcrunch","beer","duct tape","lotion","beer"}
print(groceryset) #print {'beer', 'starcrunch', 'milk', 'lotion', 'duct tape', 'cereal'}
if "milk" in groceryset:
	print("Yes I have milk")
for eachgroceryset in groceryset:
	print(eachgroceryset)
classmatesdictionary = {"Tony":"cool but smells","Emma":"sits behind me","Lucy":"asks too many questions"}
print(classmatesdictionary) #print {'Lucy': 'asks too many questions', 'Emma': 'sits behind me', 'Tony': 'cool but smells'}
print(classmatesdictionary["Emma"]) #print sits behind me
for key, value in classmatesdictionary.items():
	print(key+" "+value) #print Lucy asks too many questions\n Tony cool but smells\n Emma sits behind me

filewrite = open("sample.txt","w")
filewrite.write("Writing some stuff in my text file.\n")
filewrite.write("I like bacon.\n")
filewrite.close()
fileread = open("sample.txt","r")
text = fileread.read()
print(text) #print Writing some stuff in my text file.\n I like bacon.
fileread.close()
print("\n")

try:
	#number = int("I'm a string.")
	number = (5/0)
	#number = 50/100
	print(number)
except ValueError:
	print("You're an integer.")
except ZeroDivisionError:
	print("Can't divide by zero")
except:
	print(r"99% avoid generic or general except: according to instructor")
finally:
	print("Successful.  No matter if code work or doesn't, the print statement is printed")

class Enemy:
	life = 3
	def attack(self):
		print("ouch")
		self.life -= 1
	def checklife(self):
		if self.life <= 0:
			print("I am dead")
		else:
			print(str(self.life) + " life left")
objectenemy1 = Enemy()
objectenemy2 = Enemy()
objectenemy1.attack()
objectenemy1.attack()
objectenemy1.checklife() #return 1 life left
objectenemy2.checklife() #return 3 life left
class Tuna:
	def __init__(self):
		print("Blrrblrlbrlbrbr")
	def swim(self):
		print("I am swimming")
flipper = Tuna()
flipper.swim() #print Blrrblrlbrlbrbr\n I am swimming
class Enemy2:
	def __init__(self, x):
		self.energy = x
	def getenergy(self):
		print(self.energy)
jason = Enemy2(5)
sandy = Enemy2(18)
jason.getenergy() #return 5
sandy.getenergy() #return 18
class Girl:
	gender = "female"
	def __init__(self, name):
		self.name = name #self.name is an instance variable
rachel = Girl("Rachel")
stanky = Girl("Stanky")
print(rachel.gender) #print female
print(stanky.gender) #print female
print(rachel.name) #print Rachel
print(stanky.name) #print Stanky
class Parent():
	def printlastname(self):
		print("Roberts")
class Child(Parent): #class Child(Parent) inherits def printlastname(self)
	def printfirstname(self):
		print("Bucky")
	# def printlastname(self):
	# 	print("Snitzleberg")
bucky = Child()
bucky.printlastname() #return Roberts; however, if def printlastname(self): print("Snitzleberg") is uncommented, then return Snitzleberg because Child(Parent)'s def printlastname(self) overrides Parent() def printlastname(self)
bucky.printfirstname() #return Bucky
class Mario():
	def move(self):
		print("I am moving")
class Shroom():
	def eatshroom(self):
		print("Now I am big")
class BigMario(Mario, Shroom):
	def fireflower(self):
		print("put your code here.  I can fire.")
bigmario = BigMario()
bigmario.move() #return I am moving
bigmario.eatshroom() #return Now I am big
bigmario.fireflower() #return put your code here.  I can fire.
print("\n")

items = ["December 31, 2015","Bread Gloves",8.51]
print(items[0]) #print December 31, 2015
date = items[0]
print(date) #print December 31, 2015
date, name, price = ["December 31, 2015","Bread Gloves",8.51]
print(name) #print Bread Gloves
def dropfirstlast(grades):
	first, *middle, last = grades #first index is saved in first, last index is saved in last, the rest are saved in *middle
	avg = sum(middle) / len(middle)
	print(avg)
dropfirstlast([65, 76, 98, 54, 21]) #return 76.0.  65 saved in first, 21 saved in last, averaged 76, 98, 54 is 76.0
dropfirstlast([65, 76, 98, 54, 21, 54, 65, 99, 88, 78]) #return 69.375  65 saved in first, 78 saved in last, averaged 76, 98, 54, 21, 54, 65, 99, 88 is 69.375.
first = ["Bucky","Tom","Taylor"]
last = ["Roberts","Hanks","Swift"]
names = zip(first, last) #zip creates a list of tuples [("Bucky","Roberts"),("Tom","Hanks"),("Taylor","Swift")]
print(names) #print <zip object at 0x7f6a8a7c6848>
for a, b in names:
	print(a) #print Bucky
	print(b) #print Roberts
	print(a, b) #print Bucky Roberts
numbersa = [1, 5, 10, 79]
numbersb = [2, 3, 42, 79]
numbersab = zip(numbersa, numbersb)
for numbersa, numbersb in numbersab:
	if numbersa > numbersb:
		print(numbersa)
	elif numbersa < numbersb:
		print(numbersb)
	else:
		print(numbersa,"two equal numbers.")
"""
2
5
42
79 two equal numbers.
"""
answer = lambda x: x*7
print(answer(5)) #print 35
stocks = {
	"GOOG": 520.54,
	"FB": 76.45,
	"YHOO": 39.28,
	"AMZN": 306.21,
	"AAPL": 99.76
}
#create two lists using zip().  One list stock ticker which is key.  Second list stock price which is value.  Sorting is done by ticker.  However, a person can create one list stock price is key and second list stock ticker is value for which soring is done by price.  Zip takes the two lists and create a tuple.  zip(stocks.values(),stocks.keys()) 
print(min(zip(stocks.values(),stocks.keys()))) #print (39.28, 'YHOO') minimum stock price
print(min(zip(stocks.keys(),stocks.values()))) #print (('AAPL', 99.76) minimum stock ticker
print(max(zip(stocks.keys(),stocks.values()))) #print ('YHOO', 39.28)
print(sorted(zip(stocks.keys(), stocks.values()))) #print [('AAPL', 99.76), ('AMZN', 306.21), ('FB', 76.45), ('GOOG', 520.54), ('YHOO', 39.28)]
income = [10, 30, 75]
def doublemoney(dollars):
	return dollars * 2
for eachincome in income:
	print(doublemoney(eachincome)) #print 20\n 60\n 150
print(map(doublemoney, income)) #print <map object at 0x7f0efcf11588>
newincome = list(map(doublemoney, income))
print(newincome) #print [20, 60, 150]
import heapq
grades = [32, 43, 654, 34, 132, 66, 99, 532]
print(heapq.nlargest(1, grades)) #print [654]
print(heapq.nlargest(3, grades)) #print [654, 532, 132]
print(heapq.nsmallest(2, grades)) #print [32, 34]
stocks = [
{"ticker": "AAPL", "PRICE": 201},
{"ticker": "GOOG", "PRICE": 800},
{"ticker": "F", "PRICE": 54},
{"ticker": "MSFT", "PRICE": 313},
{"ticker": "TUNA", "PRICE": 68}
]
print(heapq.nsmallest(2, stocks, key=lambda stock:stock["PRICE"])) #print [{'ticker': 'F', 'PRICE': 54}, {'ticker': 'TUNA', 'PRICE': 68}]
print(heapq.nsmallest(2, stocks, key=lambda a:a["PRICE"])) #print [{'ticker': 'F', 'PRICE': 54}, {'ticker': 'TUNA', 'PRICE': 68}]
print(heapq.nlargest(2, stocks, key=lambda ahh:ahh["ticker"])) #print [{'ticker': 'TUNA', 'PRICE': 68}, {'ticker': 'MSFT', 'PRICE': 313}]
stocks = {
	"GOOG": 434,
	"AAPL": 325,
	"FB": 54,
	"AMZN": 623,
	"F": 32,
	"MSFT": 549,
}
print(min(stocks)) #print AAPL
stockszip = list(zip(stocks.values(),stocks.keys()))
print(stockszip) #print [(325, 'AAPL'), (549, 'MSFT'), (623, 'AMZN'), (434, 'GOOG'), (54, 'FB'), (32, 'F')]
print(min(stockszip)) #print (32, 'F')
quickerwayminstockszip = min(zip(stocks.values(),stocks.keys()))
print(quickerwayminstockszip) #print (32, 'F')
from collections import Counter
text = "We hope to one day become the world's leader in free, education resources.  We are constantly " \
"discovering and adding more free content to the website everyday.  There is already an enormous " \
"amount of resoruces online that can be accessed for free by anyone in the world, the main issue " \
"right now is that very little of it is organized or structured in any way.  We want to be the " \
"solution to that problem."
words = text.split()
print(words) #print ['We', 'hope', 'to', 'one', 'day', 'become', 'the', "world's", 'leader', 'in', 'free,', 'education', 'resources.', 'We', 'are', 'constantly', 'discovering', 'and', 'adding', 'more', 'free', 'content', 'to', 'the', 'website', 'everyday.', 'There', 'is', 'already', 'an', 'enormous', 'amount', 'of', 'resoruces', 'online', 'that', 'can', 'be', 'accessed', 'for', 'free', 'by', 'anyone', 'in', 'the', 'world,', 'the', 'main', 'issue', 'right', 'now', 'is', 'that', 'very', 'little', 'of', 'it', 'is', 'organized', 'or', 'structured', 'in', 'any', 'way.', 'We', 'want', 'to', 'be', 'the', 'solution', 'to', 'that', 'problem.']
counter = Counter(words)
topthree = counter.most_common(3)
print(topthree) #print [('the', 5), ('to', 4), ('in', 3)]
from operator import itemgetter
users = [
	{"fname": "Bucky", "lname": "Roberts"},
	{"fname": "Tom", "lname": "Roberts"},
	{"fname": "Bernie", "lname": "Zunks"},
	{"fname": "Jenna", "lname": "Hayes"},
	{"fname": "Sally", "lname": "Jones"},
	{"fname": "Amanda", "lname": "Roberts"},
	{"fname": "Tom", "lname": "Williams"},
	{"fname": "Dean", "lname": "Hayes"},
	{"fname": "Bernie", "lname": "Barbie"},
	{"fname": "Tom", "lname": "Jones"},
]
for x in sorted(users, key=itemgetter("fname")):
	print(x)
"""
{'fname': 'Amanda', 'lname': 'Roberts'}
{'fname': 'Bernie', 'lname': 'Zunks'}
{'fname': 'Bernie', 'lname': 'Barbie'}
{'fname': 'Bucky', 'lname': 'Roberts'}
{'fname': 'Dean', 'lname': 'Hayes'}
{'fname': 'Jenna', 'lname': 'Hayes'}
{'fname': 'Sally', 'lname': 'Jones'}
{'fname': 'Tom', 'lname': 'Roberts'}
{'fname': 'Tom', 'lname': 'Williams'}
{'fname': 'Tom', 'lname': 'Jones'}
"""
print("-----")
for x in sorted(users, key=itemgetter("fname","lname")):
	print(x)
"""
{'fname': 'Amanda', 'lname': 'Roberts'}
{'fname': 'Bernie', 'lname': 'Barbie'}
{'fname': 'Bernie', 'lname': 'Zunks'}
{'fname': 'Bucky', 'lname': 'Roberts'}
{'fname': 'Dean', 'lname': 'Hayes'}
{'fname': 'Jenna', 'lname': 'Hayes'}
{'fname': 'Sally', 'lname': 'Jones'}
{'fname': 'Tom', 'lname': 'Jones'}
{'fname': 'Tom', 'lname': 'Roberts'}
{'fname': 'Tom', 'lname': 'Williams'}
"""
from operator import attrgetter
class User3:
	def __init__(self, name, y):
		self.mm = name
		self.user_id = y
	def __repr__(self):
		return self.mm+" : "+str(self.user_id)
users3 = [
	User3("Bucky", 43),
	User3("Sally", 5),
	User3("Tuna", 61),
	User3("Brian", 2),
	User3("Joby", 77),
	User3("Amanda", 9)
] #each item in list users is calling the class User
print(users3) #print [Bucky : 43, Sally : 5, Tuna : 61, Brian : 2, Joby : 77, Amanda : 9]
for eachusers in users3:
	print(eachusers)
"""
Bucky : 43
Sally : 5
Tuna : 61
Brian : 2
Joby : 77
Amanda : 9
"""
for user in sorted(users3,key=attrgetter("mm")):
	print(user)
"""
Amanda : 9
Brian : 2
Bucky : 43
Joby : 77
Sally : 5
Tuna : 61
"""
for user in sorted(users3,key=attrgetter("user_id")):
	print(user)
"""
Brian : 2
Sally : 5
Amanda : 9
Bucky : 43
Tuna : 61
Joby : 77
"""