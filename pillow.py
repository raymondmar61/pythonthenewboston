from PIL import Image

img = Image.open("IMG_5521.JPG") #open image, set as a variable to convert to pillow object
# print(img.size)
# print(img.format)

#crop pic start at upper left. (start point move right, start point move down, end point horizontal dimension not crop length, end point vertical dimension not crop length).  save crop as an object.
area = (1200, 300, 3200, 3000)
cropped_img = img.crop(area)

#img.show() #display the image function, opens the computer's default program viewing pics
cropped_img.show()