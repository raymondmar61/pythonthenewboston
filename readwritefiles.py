#newboston 23 How to Read and Write Files

#create a file sample.txt with read and write privilages
filewrite = open("sample.txt","w") #"w" is user can read and write
filewrite.write("Writing some stuff in my text file\n") #\n is new line
filewrite.write("I like bacon\n")
filewrite.close()

#reads file sample.txt and prints contents to display
fileread = open("sample.txt", "r") #"r" read only
text = fileread.read() #goes to sample.txt, reads it, and stores to variable text
print(text) #print Writing some stuff in my text file\n I like bacon
fileread.close()