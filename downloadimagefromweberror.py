#newboston 22 Download an Image from the Web
#01/12/2017 first time watching tutorial Python program successful

import random #instructor imports random because want downloading images a random file name instead of downloading with same file name.
import urllib.request #get data from websites

def download_web_image(url):
	name = random.randrange(1,1000)
	fullfilename = str(name) + ".jpg" #file saved as fullfilename which is randomnumber.jpg
	urllib.request.urlretrieve(url, fullfilename) #download image, save as fullfilename
download_web_image("http://www.innovateinfinitely.com/garlic.jpg") #paste image url to function download_web_image()


# def download_web_image(url):
# 	name = random.randrange(1,1000)
# 	full_name = str(name) + ".jpg" #filesaved as full_name which is randomnumber.jpg
# 	urllib.request.urlretrieve(url, full_name) #download image, save as full_name

# download_web_image("https://thenewboston.com/photos/users/2/original/2463a86fdf42a1681c66ba8fd6789f9d.jpg") #paste image url to function download_web_image()