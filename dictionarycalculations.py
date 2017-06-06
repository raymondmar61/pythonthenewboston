#listname = keys:values. In this case, stock symbol is keys, stock price is values
stocks = {
	"GOOG": 434,
	"AAPL": 325,
	"FB": 54,
	"AMZN": 623,
	"F": 32,
	"MSFT": 549,
}

#find cheapest stock price
print(min(stocks)) #technically correct, returned AAPL, first alphabeutically
min_price = min(zip(stocks.values(), stocks.keys()))
print(min_price)


