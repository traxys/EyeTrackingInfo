import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from itertools import product
import time

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])
	
def saveToGreyscale(img):
	grImg = rgb2gray(img)
	fig = plt.imshow(grImg,cmap = plt.get_cmap('gray'))
	fig.axes.get_xaxis().set_visible(False)
	fig.axes.get_yaxis().set_visible(False)
	plt.axis('off')
	plt.savefig('foo.png',bbox_inches='tight',pad_inches = 0)

img = mpimg.imread("scrn1.png")
#reddish = img[:, :, 2] < 0.8
#img[reddish] = [0, 0, 0, 1]

fig = plt.imshow(img)
plt.show()