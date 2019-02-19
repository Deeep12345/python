playerpos=[1,1]
class Player(Person):

	def drawPlayer(self,x,y):
		if(gameArray[2*x+1][4*y+1]!="X" and gameArray[2*x+1][4*y+1]!="/"):
				gameArray[2*x+1][4*y+1] = "B" 
				gameArray[2*x+1][4*y+2] = "B"
				gameArray[2*x+1][4*y+3] = "B"
				gameArray[2*x+1][4*y+4] = "B"
				gameArray[2*x+2][4*y+1] = "B" 
				gameArray[2*x+2][4*y+2] = "B"
				gameArray[2*x+2][4*y+3] = "B"
				gameArray[2*x+2][4*y+4] = "B"
       return
        def cp(self,x,y):
             if(gameArray[2*x+1][4*y+1]=="X" or gameArray[2*x+1][4*y+1]=="$"
	         return -1
             return 1
		
         def moveDown(self):
	 	x = playerPos[0]
	 	y = playerPos[1]
	 	if(self.checkPos(x+1,y)>0):
	 	     playerPos[0] += 1
	 	     self.drawPlayer(playerPos[0],playerPos[1])
	 	else:
	 	     print("lost live")
		return
	 def moveUp(self):
		x = playerPos[0]
		y = playerPos[1]	
		if(self.checkPos(x-1,y)>0):
		     playerPos[0] -= 1
		     self.drawPlayer(playerPos[0],playerPos[1])	
		else:
		     print("lost live")
		return
	 def moveLeft(self):
		x = playerPos[0]
		y = playerPos[1]		
		if(self.checkPos(x,y-1)>0):
			playerPos[1] -= 1
			self.drawPlayer(playerPos[0],playerPos[1])
		else:
		         print("lost live")
		return
	def moveRight(self):
		x = playerPos[0]
		y = playerPos[1]
		if(self.checkPos(x,y+1)>0):
			playerPos[1] += 1
			self.drawPlayer(playerPos[0],playerPos[1])	
		else:
		         print("lost live")
		return
		
