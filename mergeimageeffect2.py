from PIL import Image

zion = Image.open("IMG_5521.JPG")
sanborn = Image.open("IMG_5026.JPG")
rzion, gzion, bzion = zion.split() #split image in R, G, and B
rsanborn, gsanborn, bsanborn = sanborn.split() #split image in R, G, and B

#merge two channels from two images into one image
new_img = Image.merge("RGB", (rzion, gzion, bsanborn))
new_img.show()