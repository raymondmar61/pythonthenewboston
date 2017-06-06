from PIL import Image

zion = Image.open("IMG_5521.JPG")
earthquakes = Image.open("IMG_4990.JPG")

#paste pic start at upper left. (start point move right, start point move down, end point horizontal dimension not crop length, end point vertical dimension not crop length
area = (2000, 300, 2600, 800) #being paste at (2000, 300), paste to 2600 horizontal and 800 vertical
zion.paste(earthquakes, area) #paste earthquakes pic on top of zion pic location defined by area

zion.show()