pps=[1,1]
class Player(Person):

	def drawPlayer(self,x,y):
		if(gameArray[2*x+1][4*y+1]!="X" and gameArray[2*x+1][4*y+1]!="1"):
				gameArray[2*x+1][4*y+1] = "B" 
				gameArray[2*x+1][4*y+2] = "B"
				gameArray[2*x+1][4*y+3] = "B
				gameArray[2*x+2][4*y+1] = "B" 
				gameArray[2*x+2][4*y+2] = "B"
				gameArray[2*x+2][4*y+3] = "B"
       return

        def cp(self,x,y):
             if(gameArray[2*x+1][4*y+1]=="X" or gameArray[2*x+1][4*y+1]=="1"
	         return -1
             return 1
		
	def playerInit(self):
		pps[0] = 1
		pps[1] = 1
		x = pps[0]
		y = pps[1]
		return	
		
         def moveDown(self):
	 	x = pps[0]
	 	y = pps[1]
	 	if(self.cp(x+1,y)>0):
	 	     pps[0] += 1
	 	     self.drawPlayer(pps[0],pps[1])
	 	else:
	 	     print("lost live")
		return
		
	 def moveUp(self):
		x = pps[0]
		y = pps[1]	
		if(self.cp(x-1,y)>0):
		     pps[0] -= 1
		     self.drawPlayer(pps[0],pps[1])	
		else:
		     print("lost live")
		return
		
	 def moveLeft(self):
		x = pps[0]
		y = pps[1]		
		if(self.cp(x,y-1)>0):
			pps[1] -= 1
			self.drawPlayer(pps[0],pps[1])
		else:
		         print("lost live")
		return
		
	def moveRight(self):
		x = pps[0]
		y = pps[1]
		if(self.cp(x,y+1)>0):
			pps[1] += 1
			self.drawPlayer(pps[0],pps[1])	
		else:
		         print("lost live")
		return
		
