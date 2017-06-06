#newboston 12 Functions
#newboston 13 Return Values
#newboston 14 Default Values for Arguments
#newboston 16 Keyword Arguments
#newboston 17 Flexible Number of Arguments
#newboston 18 Unpacking Arguments

#Run functions.py in terminal type "python3.4 functions.py"
#Functions And Calling A Function
def beef():
	print("Dayum, functions are cool!")
	pass
beef() #return Dayum, functions are cool!

#Function Returning Values
def bitcoin_to_usd(btc):
	amount = btc * 527
	print(amount)
	pass
bitcoin_to_usd(3.85)  #return 2028.95

def allowed_dating_age(my_age):
	girls_age = (my_age/2) + 7
	return girls_age
buckys_limit = allowed_dating_age(27)
print("Bucky can date girls", buckys_limit, "or older") #print Bucky can date girls 20.5 or older

# bonus for loop from bucky
# for eachages in range(18,101):
# 	age_limit = allowed_dating_age(eachages)
# 	print("A man age" ,eachages, "can date girls", age_limit, "or older")

#Default Values For Arguments
def get_gender(sex="Unknown"): #default value is Unknown
	if sex is "m":
		sex = "Male"
	elif sex is "f":
		sex = "Female"
	print(sex)
get_gender("m") #return Male
get_gender("f") #return Female
get_gender() #return Unknown

#Keyword Arguments
def dumb_sentence(name="Bucky", action="ate", item="tuna"):
	print(name, action, item)
dumb_sentence() #return Bucky ate tuna
dumb_sentence("Sally","farts","gently") #return Sally farts gently
dumb_sentence(item="awesome", action="is") #return Bucky is awesome

 #* take an x number of arguments args
def add_numbers(*args):
	totalsum = 0
	for eachargs in args:
		totalsum += eachargs
	print(totalsum)
	pass
add_numbers(3) #return 3
add_numbers(3, 32) #return 35
add_numbers(3, 43, 5453, 354234, 463463) #return 823196

#Unpacking Arguments
def health_calculator(age, apples_ate, cigs_smoked):
	answer = (100-age) + (apples_ate * 3.5) - (cigs_smoked * 2)
	print(answer)
	pass
buckys_data = [27, 20, 0]
health_calculator(buckys_data[0],buckys_data[1],buckys_data[2]) #return 143.0
health_calculator(*buckys_data) #return 143.0 #Use *, faster than typing each list