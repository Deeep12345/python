import sys
from board import *
from player import *
from wall import *
from bomb import *


inp=input("press any key w,a,s,d,b")
if(inp == 'q'):
		sys.exit(0)		#Quits
	elif(inp == 's'):
		pl.moveDown()	#moves the player down on pressing 's'
	elif(inp == 'w'):
		pl.moveUp()		#moves the player up on pressing 'w'
	elif(inp == 'a'):
		pl.moveLeft()	#moves the player left on pressing 'a'
	elif(inp == 'd'):
		pl.moveRight()	#moves the player right on pressing 'd'
