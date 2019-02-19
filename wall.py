from random import randint
from board import *

wallPos = []

class wall(Board):


	def wallinit(self):
		for i in range(20):
			x = randint(1,6)
			y = randint(1,6)	
			wallPos.append([x,y])
		return

	def drawwalls(self):
		size = len(wallPos)
		for i in range(size):
			x = wallPos[i][0]
			y = wallPos[i][1]
			
			if(x*y!=1 and (ga[2*x+1][4*y+1]!="X" )):
				ga[2*x+1][4*y+1] ="1" 
				ga[2*x+1][4*y+2] = "1"
				ga[2*x+1][4*y+3] = "1"
				ga[2*x+2][4*y+1] = "1"
				ga[2*x+2][4*y+2] = "1"
				ga[2*x+2][4*y+3] = "1"
				#for wall to be represented by 1
