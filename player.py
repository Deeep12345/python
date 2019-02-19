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
		       if(gameArray[2*x+1][4*y+1]=="X" or gameArray[2*x+1][4*y+1]=="/"):
			                return -1
		       return 1   
