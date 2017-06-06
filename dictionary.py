#newboston 20 Dictionary, 41 Min, Max and Sorting Dictionaries, 52-53 Finding Largest or Smallest Items, 53 Dictionary Calculations, 55 Dictionary Multiple Key Sort

#{key k:value v} separated by commas inside curly braces
classmates = {"Tony":"cool but smells","Emma":"sits behind me", "Lucy":"asks too many questions"}
print(classmates) #print {'Lucy': 'asks too many questions', 'Emma': 'sits behind me', 'Tony': 'cool but smells'}
print(classmates["Emma"]) #print sits behind me #prints value sits behind me from key Emma
for k, v in classmates.items():
	print(k+" "+v) #print each key and value in its own line in no particular order
	pass

stocks = {"GOOG": 520.54, "FB": 76.45, "YHOO": 39.28, "AMZN": 305.21, "AAPL": 99.76}
zip(stocks.values(), stocks.keys())
print(zip(stocks.values(), stocks.keys())) #print <zip object at 0x7fb064cf6948>
print(min(zip(stocks.values(), stocks.keys()))) #print (39.28, 'YHOO')
print(max(zip(stocks.values(), stocks.keys()))) #print (520.54, 'GOOG')
print(sorted(zip(stocks.values(), stocks.keys()))) #print [(39.28, 'YHOO'), (76.45, 'FB'), (99.76, 'AAPL'), (305.21, 'AMZN'), (520.54, 'GOOG')] values sorted smallest to largest
print(sorted(zip(stocks.keys(), stocks.values()))) #print [('AAPL', 99.76), ('AMZN', 305.21), ('FB', 76.45), ('GOOG', 520.54), ('YHOO', 39.28)] keys sorted smallest to largest

import heapq

stocks = [
{"ticker": "AAPL", "PRICE": 201},
{"ticker": "GOOG", "PRICE": 800},
{"ticker": "F", "PRICE": 54},
{"ticker": "MSFT", "PRICE": 313},
{"ticker": "TUNA", "PRICE": 68}
]
print(heapq.nsmallest(2,stocks, key=lambda stock: stock["PRICE"])) #print [{'PRICE': 54, 'ticker': 'F'}, {'PRICE': 68, 'ticker': 'TUNA'}]

#listname = keys:values. In this case, stock symbol is keys, stock price is values
stocks = {
	"GOOG": 434,
	"AAPL": 325,
	"FB": 54,
	"AMZN": 623,
	"F": 32,
	"MSFT": 549,
}
print(min(stocks))  #print AAPL.  Want F Ford lowest stock price.
print((zip(stocks.values(), stocks.keys()))) #print <zip object at 0x7fe60c555988>
swaplist = (zip(stocks.values(), stocks.keys()))
print(swaplist) #print <zip object at 0x7fd1dabe19c8>
min_price = min(zip(stocks.values(), stocks.keys()))
print(min_price) #print (32, 'F')

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
	print(x) #print {'fname': 'Amanda', 'lname': 'Roberts'}
# {'fname': 'Bernie', 'lname': 'Zunks'}
# {'fname': 'Bernie', 'lname': 'Barbie'}
# {'fname': 'Bucky', 'lname': 'Roberts'}
# {'fname': 'Dean', 'lname': 'Hayes'}
# {'fname': 'Jenna', 'lname': 'Hayes'}
# {'fname': 'Sally', 'lname': 'Jones'}
# {'fname': 'Tom', 'lname': 'Roberts'}
# {'fname': 'Tom', 'lname': 'Williams'}
# {'fname': 'Tom', 'lname': 'Jones'}
print("-----")
for x in sorted(users, key=itemgetter("fname","lname")):
	print(x) #print correctly sorted {'fname': 'Amanda', 'lname': 'Roberts'}
# {'fname': 'Bernie', 'lname': 'Barbie'}
# {'fname': 'Bernie', 'lname': 'Zunks'}
# {'fname': 'Bucky', 'lname': 'Roberts'}
# {'fname': 'Dean', 'lname': 'Hayes'}
# {'fname': 'Jenna', 'lname': 'Hayes'}
# {'fname': 'Sally', 'lname': 'Jones'}
# {'fname': 'Tom', 'lname': 'Jones'}
# {'fname': 'Tom', 'lname': 'Roberts'}
# {'fname': 'Tom', 'lname': 'Williams'}

