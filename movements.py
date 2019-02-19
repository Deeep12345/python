import sys
from board import *
from player import *
from wall import *
from bomb import *

p1=player()
p1.playerInit()
bom=bomb()
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
        elif(inp=='b'):
		if(bps[2] == -1):
			bps[0] = pps[0]
			bps[1] = pps[1]
			bps[2] = 3
			bom.db()
			
		
