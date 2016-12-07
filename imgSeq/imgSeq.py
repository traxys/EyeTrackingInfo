import tkinter as tk
import numpy as np
from PIL import Image, ImageTk
import time
	
def printNextImage(i):
	k = i +1
	cIStr = ""
	if k < 10:
		cIStr = "00"+str(k)
	elif k < 100:
		cIStr = "0"+str(k)
	else:
		cIStr = str(k)
	
	img = plt.imread("image-"+cIStr+".png")
	
	plt.clf()
	plt.imshow(img)
	fig.canvas.draw()	
	
def playAnimation():
	timeSpent = []
	for k in range(1,269):
		startTime = time.clock()
		
		cIStr = ""
		if k < 10:
			cIStr = "00"+str(k)
		elif k < 100:
			cIStr = "0"+str(k)
		else:
			cIStr = str(k)
			
		img = Image.open("image-"+cIStr+".png")
		img_tk = ImageTk.PhotoImage(img)
		label.configure(image=img_tk)
		label.image = img_tk
		root.update_idletasks()
		
		timeSpent.append(time.clock()-startTime)
		
		#time.sleep(1/25)
	print(np.mean(timeSpent))
	
root = tk.Tk()
label = tk.Label(root)
label.pack()
img = Image.open("image-001.png")
btn = tk.Button(root,text="Start",command=playAnimation)
btn.pack()
img_tk = ImageTk.PhotoImage(img)
label.config(image=img_tk)

#Tkinter version
root.mainloop()

#Matplotlib version
#fig = plt.figure()
#a = anim.FuncAnimation(fig,printNextImage,frames=268,repeat=False,interval=1)
#plt.show()
