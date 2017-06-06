#take any list and run all items in a function individually

income = [10, 30, 75]

def double_money(dollars):
	return dollars * 2

#goes through each item in list income[] to input in function double_money()
new_income = list(map(double_money, income))
print(new_income)

#for loop also works
#for item in income:
