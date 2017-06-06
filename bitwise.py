# Binary AND.  Also works for OR using | instead of &

a = 50 #50 binary is 110010
b = 25 #25 binary is 011001
c = a & b #c "ands" a & b togehter 110010 + 011001= 010000; 1 + 1 = 1 otherwise 0
print(c) #answer is 16

# Binary RIGHT SHIFT.  Also works for LEFT SHIFT using << instead of >>

x = 240 #11110000
y = x >> 2 #shift binary x=240 two numbers to the right which results in 00111100
print(y) #answer is 60

#there is an online binary calculator to check answers