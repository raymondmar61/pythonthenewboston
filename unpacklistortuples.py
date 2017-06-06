#newboston 38 Unpack List or Tuples

item = ["December 23, 2015","Bread Gloves",8.51]
print(item[1]) #prints Bread Gloves

#set each element in a list to a variable.  Unpacking a list into variables.
date, name, price = ["December 23, 2015","Bread Gloves",8.51]
print(name) #prints Bread Gloves

#set some elements in a list to a variable
date, *name, price = ["December 23, 2015","Bread Gloves","Foot Gloves","Yum","Fish",8.51]
print(name) #prints ['Bread Gloves', 'Foot Gloves', 'Yum', 'Fish']

def drop_first_last(grades):
	first, *middle, last = grades
	print(grades)  #prints [65, 76, 98, 54, 21]
	avg = sum(middle) / len(middle)
	print(avg)
drop_first_last([65, 76, 98, 54, 21]) #returns 76.0.  65 is first, 21 is last, rest is middle.  76, 98, 54 average is 76. first and last in list are dropped.  Example wasn't drop highest and lowest.  Drop first and last.