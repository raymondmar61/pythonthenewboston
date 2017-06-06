from PIL import Image

zion = Image.open("IMG_5521.JPG")
print(zion.mode) #RGB channel or CMYK channel?
r, g, b = zion.split() #split image in R, G, and B

#merge RGB three images into one in RGB channel order
new_image = Image.merge("RGB", (r, g, b))
new_image.show()

#merge RGB three images into one in BGR channel order
new_image = Image.merge("RGB", (b, g, r))
new_image.show()

