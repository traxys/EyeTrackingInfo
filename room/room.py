from PIL import Image, ImageTk
import numpy as np
import tkinter as tk
from random import randrange

import progressbar

#import matplotlib.pyplot as plt

def loadRoom():
	'''Returns an array containg 359 frames as PIL objects'''
	
	bar = progressbar.ProgressBar(
	widgets=[
		"Loading Room",
		progressbar.Bar(),
		"(",progressbar.ETA(),")"
	],
	max_value=360)
	
	room = []
	name = "Loading Room"
	for i in bar(range(1,361)):
		room.append( Image.open("deg_"+str(i)+".png") )
	return room

def getRoomAsNP():
	room = loadRoom()
	npRoom = []
	bar = progressbar.ProgressBar(
	widgets=[
		"Converting Room",
		progressbar.Bar(),
		"(",progressbar.ETA(),")"
	],
	max_value=360)
	for i in bar(room):
		npRoom.append(np.array(i))
	return np.array(npRoom)
	
def showImage():
	t = randrange(359)
	img_tk = ImageTk.PhotoImage(room[t])
	label.configure(image=img_tk)
	label.image = img_tk
	
root = tk.Tk()
label = tk.Label(root)
label.pack()
btn = tk.Button(root,text="Start",command=showImage)
btn.pack()
room = loadRoom()

root.mainloop()