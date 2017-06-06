print("hello world print() is a function") #hello world print() is a function
print(len("hello world")) #11
print(5**3) #125
x = 10
print(x*4) #40
tuna = 5
print(tuna+20) #25
bacon = 75
print(bacon/tuna) #15
print("I don't ""think"" she's 55") #I don't think she's 55
print("c:\Mar\Desktop\python") #c:\Mar\Desktop\python
user = "Raymond Mar Python starts at zero 0"
print(user) #Raymond Mar Python starts at zero 0
print(user[0]) #R
print(user[3:7]) #mond R0 a1 y2 m3 o4 n5 d6
print(user[:6]) #Raymon R0 a1 y2 m3 o4 n5 d6

playerlist = [29, 58, 66, 71, 87]
print(playerlist[2]) #66
print(playerlist + [90, 91, 98]) #[29, 58, 66, 71, 87, 90, 91, 98]
print(playerlist) #[29, 58, 66, 71, 87]
playerlist.append(120) 
print(playerlist) #[29, 58, 66, 71, 87, 120]
print(playerlist[:2]) #[29, 58]
playerlist[:2] = [0 ,1]
print(playerlist) #[0 ,1, 66, 71, 87, 120]
playerlist[:2] = []
print(playerlist) #[66, 71, 87, 120]
playerlist[:]=[]
print(playerlist) #[]