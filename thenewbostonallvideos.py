#The New Boston 2 Numbers, 3 Strings, 4 Slicing up Strings, 5 Lists, 7 if elif else, 8 for, 9 Range and While, 

"""
print(18/3.4) #print 5.294117647058823
print(18//3.4) #print 5.0
print(18/4) #print 4.5
print(18//4) #print 4
print(18/4.1) #print 4.390243902439025
print(18//4.1) #print 4.0
print(18/4.4) #print 4.090909090909091
print(18//4.4) #print 4.0
"""
print(18/5) #print 3.6
print(18//5) #print 3
print(18//5.0) #print 3.0
print(18/8) #print 2.25
print(18//8) #print 2
print(r"this story is \nokday d'kay") #print this story is \nokday d'kay
user = "Tuna McFish"
print(user[0]) #print T
print(user[1:4]) #print una
print(user[1:9:2]) #print uaMF
print(user[-1]) #print h
print(user[-1::-1]) #print hsiFcM anuT
players = [29, 58, 66, 71, 87]
print(players[2]) #print 66
players[2] = 68
print(players[2]) #print 68
newplayers = players + [90, 91, 98]
newplayers.append(120)
print(newplayers) #print [29, 58, 68, 71, 87, 90, 91, 98, 120]
newplayers[6:] = [-1, -2, -3]
print(newplayers) #print [29, 58, 68, 71, 87, 90, -1, -2, -3]
newplayers[5:] = []
print(newplayers) #print [29, 58, 68, 71, 87]
name = "Bucky"
if name is "Bucky":
	print("Hey there Bucky")
if "uck" in name:
	print("Hey there uck")
players = [29, 58, 66, 71, 87]
for eachplayers in players[0:3]:
	print(eachplayers) #print 29\n 58\n 66
for eachnumber in range(100,-51,-25):
	print(eachnumber,end=", ") #print 100, 75, 50, 25, 0, -25, -50,
print("\n")
def functioname(number):
	return number+50
print(functioname(150)) #print 200