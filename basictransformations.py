from PIL import Image

family = Image.open("IMG_0973.JPG")

#resize image.  New dimensions.  In this case, 50% smaller from original.
square_family = family.resize((1296, 972))

#flip image. Image.FLIP_LEFT_RIGHT or Image.FLIP_TOP_BOTTOM
flip_family = family.transpose(Image.FLIP_LEFT_RIGHT)

#rotate.  Image.ROTATE_180, Image.ROTATE_270, or Image.ROTATE_90
rotate_family = family.transpose(Image.ROTATE_90)

family.show()
square_family.show()
flip_family.show()
rotate_family.show()