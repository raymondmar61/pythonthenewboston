from PIL import Image
from PIL import ImageFilter

family = Image.open("IMG_0973.JPG")

#convert to black & white--> imagename.convert("L")
black_white = family.convert("L")

#from ImageFilter class, call BLUR
blur = family.filter(ImageFilter.BLUR)

#from ImageFilter class, call DETAIL
detail = family.filter(ImageFilter.DETAIL)

#from ImageFilter class, call FIND_EDGES
edges = family.filter(ImageFilter.FIND_EDGES)

blur.show()
detail.show()
edges.show()
