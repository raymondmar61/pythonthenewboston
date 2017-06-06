#newboston 39 Zip

#two lists equal length and tie them togehter or zip them together
first = ["Bucky","Tom","Taylor"]
last = ["Roberts","Hanks","Swift"]
names = zip(first, last)
for a, b in names: #a is first, b is last in for loop
	print(a, b) #prints Bucky Roberts\n Tom Hanks\n, Taylor Swift
