from skimage.io import imread,imsave
from skimage import color

img = imread('horse.jpg')
img_new = color.rgb2gray(img)

imsave('horse_gray.jpg',img_new)
# TODO: add basic image processing operations performed using skimage
