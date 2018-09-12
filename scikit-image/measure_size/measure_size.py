# import required modules:

from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import numpy as np
import argparse
import imutils
import skimage

# argument parse construction#
# use this part to pass parameters like filepath and default height/width to externally run program
#from command line
ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required=True,
                help='path to input image')
ap.add_argument('-w','--width',type=float,required=False,
                help='width of the left-most object in the image')
ap.add_argument('-p','--pxpermetric',type=float,required=False,
                help='pixels per metric if known (use for only fixed camera-object pairs)')
args = vars(ap.parse_args())

# load the image, convert it to grayscale, and blur it slightly
image = skimage.io.imread(args["image"])
gray = skimage.color.rgb2gray(image)
gray = skimage.filters.gaussian(gray)
# TODO: blur image using skimage
