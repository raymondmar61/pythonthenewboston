from PIL import Image

zion = Image.open("IMG_5521.JPG")
print(zion.mode) #RGB channel or CMYK channel?
r, g, b = zion.split() #split image in R, G, and B

r.show() #show image as red channel
g.show() #show image as green channel
b.show() #show image as blue channel