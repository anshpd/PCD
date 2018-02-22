from PIL import Image
import PIL.ImageOps


img = Image.open('image1.jpg')

# inverted image
inverted_image = PIL.ImageOps.invert(img)
inverted_image.save('new-img.jpg')

# contrast image
img_ctr = PIL.ImageOps.autocontrast(img, cutoff=123)
img_ctr.save('new-contrast.jpg')

#equalize image
img_equ = PIL.ImageOps.equalize(img)
img_equ.save('equalize-img.jpg')

