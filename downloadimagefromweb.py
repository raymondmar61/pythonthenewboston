import random
import urllib.request #get data from websites

def download_web_image(url):
	name = random.randrange(1,1000)
	full_name = str(name) + ".jpg" #filesaved as full_name which is randomnumber.jpg
	urllib.request.urlretrieve(url, full_name) #download image, save as full_name

download_web_image("https://thenewboston.com/photos/users/2/original/2463a86fdf42a1681c66ba8fd6789f9d.jpg") #paste image url to function download_web_image()