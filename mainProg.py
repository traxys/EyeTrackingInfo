import numpy as np
#Pour charger , et gerer les images
from PIL import Image, ImageTk
import tkinter as tk

from time import sleep

#Ca fait joli
import progressbar

#Temps d'attente entre chaque iteration
LOOP_DELAY = 10

#Salle en 360 degré par dessus laquelle on peut superposer le cube
def loadRoom(hasBar=True):
	'''Returns an array containg 359 frames as PIL objects'''
	room = []
	if hasBar:
		bar = progressbar.ProgressBar(
		widgets=[
			"Loading Room",
			progressbar.Bar(),
			"(",progressbar.ETA(),")"
		],
		max_value=360)
		
		name = "Loading Room"
		for i in bar(range(1,361)):
			room.append( Image.open("room/deg_"+str(i)+".png") )
	else:
		for i in range(1,361):
			room.append( Image.open("room/deg_"+str(i)+".png") )
	return room

#Entrée et sortie de la boucle
runTrack = 0
def stopTrack():
	'''Tk event func'''
	global runTrack
	runTrack = -1
def startTrack():
	'''Tk event func'''
	global runTrack
	runTrack = 1

#Boucle principal du programme
def eyeTrack():
	'''Main loop , called by tk'''
	global runTrack
	if runTrack == 1:
		btnStart.pack_forget()
		btnEnd = tk.Button(root,text="Stop",command=stopTrack)
		btnEnd.pack()
		runTrack = 2
	
	if runTrack == 2:
		#Appel des Fonctions Ici , le reste est pour gerer la boucle
		print("In loop")
		#Fin de la zone d'appel des fonctions
		
		root.update_idletasks()
		root.after(LOOP_DELAY,eyeTrack)
	
	elif runTrack == 0:
		root.after(LOOP_DELAY,eyeTrack)
	else:
		#Termine le programme
		quit()

print("(1) Mode matplotlib\n(2) Mode superposition")
mode = 0
while not (mode == 1 or mode == 2):
	try:
		mode = int(input("Mode :"))
	except Exception:
		pass
	if not (mode == 1 or mode == 2):
		print("Entrée Incorecte",end=' , ')

#Mode avec Tkinter
if mode == 2:	
	#Mise en place du GUI
	root = tk.Tk()
	label = tk.Label(root)
	label.pack()
	btnStart = tk.Button(root,text="Start",command=startTrack)
	btnStart.pack()

	#Chargement de la salle avant le lancement du GUI
	room = loadRoom(False)

	#Lancement initiale de la boucle
	root.after(0,eyeTrack)
	#Lancement du GUI Tkinter , tout code ecrit apres cette ligne est inutile
	root.mainloop()