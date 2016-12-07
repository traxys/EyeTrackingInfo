import numpy as np
import matplotlib.pyplot as plt

from collections import namedtuple
Point = namedtuple("Point",["x","y"])
Angle = namedtuple("Angle",["x","y"])

def getAngle(pos):
	"""Input : position=[x , y] ou 0<=x<=1 et 0<=y<=1
Output : angle=[x , y] ou -pi/4<=x<=pi/4 et -pi/4<=y<=pi/4"""
	return Angle( np.arctan((pos.x-0.5)/0.5) , np.arctan((pos.y-0.5)/0.5) )
	
def getAngleDegree(pos):
	"""getAngle avec l'output en degrée"""
	return Angle(getAngle(pos).x*(180/np.pi),getAngle(pos).y*(180/np.pi))