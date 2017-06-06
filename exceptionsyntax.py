# tuna = int(input("What's your favorite number?\n")) #int means integer
# print(tuna) #ValueError is a type of Exception Error; error happens when user types a nonnumber

while True:
	try:
		number = int(input("What's your favorite number hoss?\n"))
		print(18/number)
		break
	except ValueError:
		print("Make sure and enter a number") #if nonnumber, ValueError exception error appeared, repeat while loop
	except ZeroDivisionError:
		print("Don't pick zero") #if zero, ZeroDivisionError exception error appeared, repeat while loop
	except:
		break #the "except *no specified exception error*:" covers all exception errors
	finally:
		print("loop complete") #no matter if the code work or an exception error, run the code below "finally:"
	pass