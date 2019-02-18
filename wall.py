wallPos = []

class Brick(Board):


	def brickInit(self):
		for i in range(20):
			x = randint(1,6)
			y = randint(1,6)	
			brickPos.append([x,y])
		return

	def drawBricks(self):
		size = len(brickPos)
		for i in range(size):
			#print(i,"\n")
			x = brickPos[i][0]
			y = brickPos[i][1]
			
			if(x*y!=1 and (ga[2*x+1][4*y+1]!="X" )):
				ga[2*x+1][4*y+1] ="$" 
				ga[2*x+1][4*y+2] = "$"
				ga[2*x+1][4*y+3] = "$"
				ga[2*x+1][4*y+4] = "$"
				ga[2*x+2][4*y+1] = "$"
				ga[2*x+2][4*y+2] = "$"
				ga[2*x+2][4*y+3] = "$"
				ga[2*x+2][4*y+4] = "$"
