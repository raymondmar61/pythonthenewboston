#newboston 8 for
#newboston 10 Comments and Break
#newboston 11 Continue

foods = ["bacon","tuna","ham","sausages","beef"]
for eachfood in foods:
	print(eachfood)
	print(len(eachfood) ,"characters.")
	pass
print("\n")
for eachfood in foods[:2]: #prints bacon, tuna only
	print(eachfood)
	print(len(eachfood) ,"characters.")
	pass

magicNumber = 26
for eachn in range(0,101):
	if eachn is magicNumber:
		print(eachn, "is the magic number!")
		break
	else:
		print(eachn)
print("\n")

for eachnumber in range(1,101):
	if eachnumber % 4 == 0:
		print(eachnumber)
print("\n")

#bonus for loop below
# import random
# magicNumber = random.randint(1,100)
# for eachNumber in range(1,101):
# 	print(eachNumber)
# 	if eachNumber == magicNumber:
# 		print("The magic number is",magicNumber)
# 		break

numbersTaken = [2, 5, 12, 33, 17]
print("Here are the numbers that are still available:")
for n in range(1, 20):
	if n in numbersTaken:
		continue
	print(n) #prints numbers 1 to 19 skipping 2, 5, 12 from numbersTaken