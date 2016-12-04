import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from itertools import product #Permettre de faire un for x,y
import time #Mesurer le temps d'exec

def rgb2gray(rgb): #Transformer une image en niveaux de gris
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])
	
def saveToGreyscale(img): #Convertir une image en niveaux de gris et l'enregistrer
	grImg = rgb2gray(img)
	fig = plt.imshow(grImg,cmap = plt.get_cmap('gray'))
	fig.axes.get_xaxis().set_visible(False)
	fig.axes.get_yaxis().set_visible(False)
	plt.axis('off')
	plt.savefig('foo.png',bbox_inches='tight',pad_inches = 0)

f,axArr = plt.subplots(1,2) #Creer une zone pour afficher deux images

img = mpimg.imread("scrn1.png") #Charger l'image
axArr[0].imshow(img[::15,::15]) #Afficher l'image a l'ecran

startTime = time.clock()

img = img[::15,::15] #Downsampling by a 'n' factor

img[img[:, :, 2] < 0.8] = [0, 0, 0, 1] #Filtre bleu
rZone = img[:,:,0] > 0.5 #Filtre toute les couleurs trop importantes


#spot = np.where(img[:,:,2] != 0) #Trouver le centre de la zone bleu
#print( np.mean(spot[0]), np.mean(spot[1]))

print("Time to filter blue",time.clock()-startTime) #Mesurer le temps que cela a pris

axArr[1].imshow(img) #Afficher l'image avec le point bleu
plt.show() #Afficher le tout a l'ecran