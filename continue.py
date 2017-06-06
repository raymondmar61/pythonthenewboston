numbersTaken = [2, 5, 12, 33, 17]

print("Here are the numbers that are still available:")
for n in range(1,21):
	if n in numbersTaken: 
		continue #continue for loop. Don't print numbersTaken.
	print(n)
	pass