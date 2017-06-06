#newboston 5 Lists, 50 map, 52-53 Finding Largest or Smallest Items

players = [29, 58, 66, 71, 87]
print(players[2]) #print 66
print(players[:2]) #print [29, 58]
players[2] = 1000
print(players) #print [29, 58, 1000, 71, 87]
players[:2] = [0, 0]
print(players) #print [0, 0, 66, 71, 87]
players[:2] = []
print(players) #print [1000, 71, 87]
players[:] = []
print(players) #print []

#error message.  .append() takes exactly one argument.
# players.append(90, 91, 98)
#doesn't work
# players = [29, 58, 66, 71, 87]
# newplayers = 90, 91, 98
# players.append(newplayers)
# print(players) #print [29, 58, 68, 71, 87 ,(90, 91, 98)]
#doesn't work
# players = [29, 58, 66, 71, 87]
# newplayers = [90, 91, 98]
# players.append(newplayers)
# print(players) #print [29, 58, 68, 71, 87 ,[90, 91, 98]

players = [29, 58, 66, 71, 87]
newplayers = [90, 91, 98]
for eachnewplayers in newplayers:
	players.append(eachnewplayers) 
print(players) #print [29, 58, 68, 71, 87, 90, 91, 98]

players = [29, 58, 66, 71, 87]
players = [29, 58, 68, 71, 87 ,90, 91, 98]
print(players) #print [29, 58, 68, 71, 87, 90, 91, 98]

#map() function.  Take any list and run all items in a function individually.
income = [10, 30, 75]
def double_money(dollars):
	return  dollars * 2
print((map(double_money,income))) #print <map object at 0x7f3ff89156a0>
new_income = list(map(double_money,income))
print(new_income) #print [20, 60, 150]

#or run a for loop
newincome = []
for eachincome in income:
	eachincome = eachincome * 2
	newincome.append(eachincome)
print(newincome) #print [20, 60, 150]

import heapq
grades = [32,43,654,34,132,66,99,532]
print(heapq.nlargest(3,grades)) #print [654, 532, 132]

stocks = [
{"ticker": "AAPL", "PRICE": 201},
{"ticker": "GOOG", "PRICE": 800},
{"ticker": "F", "PRICE": 54},
{"ticker": "MSFT", "PRICE": 313},
{"ticker": "TUNA", "PRICE": 68}
]
print(heapq.nsmallest(2,stocks, key=lambda stock: stock["PRICE"])) #print [{'PRICE': 54, 'ticker': 'F'}, {'PRICE': 68, 'ticker': 'TUNA'}]