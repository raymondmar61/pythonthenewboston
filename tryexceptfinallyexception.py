#newboston 28 You are the only Exception

# tuna = int(input("What's your favorite number?\n"))
# print(tuna)

while True:
	try:
		tuna = int(input("What's your favorite number?\n"))
		print(tuna)
		break
	except ValueError:
		print("Make sure and enter a number")
	except ZeroDivisionError:
		print("Don't pick zero")
	except: #99% of time don't use it says instructor.  General except: code.
		break
	finally:
		print("finally is an optional code.  No matter if the code worked, then execute the finally.  finally occurs every time.  Loop is complete.")
