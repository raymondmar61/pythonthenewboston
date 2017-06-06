import heapq #allows to sort easily

grades = [32, 43, 654, 34, 132, 66, 99, 532]

#show the three largest grades
print(heapq.nlargest(3, grades))

stocks = [
{"ticker": "AAPL", "PRICE": 201},
{"ticker": "GOOG", "PRICE": 800},
{"ticker": "F", "PRICE": 54},
{"ticker": "MSFT", "PRICE": 313},
{"ticker": "TUNA", "PRICE": 68}
]

print(heapq.nsmallest(2, stocks, key=lambda stock:stock["PRICE"]))