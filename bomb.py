from board import *
from player import *
from movements import *
from wall import *

bps=[0,0,-1] #the position of the bomb for x , y.
b=[]
class Bomb():
  def db(self):
    x=bps[0]
    y=bps[1]
    
    if(bps[2]>-1):
      if not b:
        for i in range(1,3):
          for j in range(1,5):
                 b.append([2*x+i,4*y+j])
      ga[2*x+1][4*y+1]=bps[2]
      ga[2*x+1][4*y+2]=bps[2]
      ga[2*x+1][4*y+3]=bps[2]
      ga[2*x+2][4*y+1]=bps[2]
      ga[2*x+2][4*y+2]=bps[2]
      ga[2*x+2][4*y+3]=bps[2]
    bps[2]-=1
    if(bps[2]==-1):
      self.explosion()
    return
  def de(self,x,y):      #for the scene during explosion ,to represent the explosion scene

		ga[2*x+1][4*y+1] = "m"
		ga[2*x+1][4*y+2] = "m"
		ga[2*x+1][4*y+3] = "m"
		ga[2*x+2][4*y+1] = "m"
		ga[2*x+2][4*y+2] = "m"
		ga[2*x+2][4*y+3] = "m"		
		return
  
  def ae(self,x,y):        #for the scene after the explosion has occured
    if(x==pps[0] and y==pps[1]):
      print("lost live")
    elif([x,y] in wallPos):
      wallPos.remove([x,y])
     
   return
  
  def cp(self,x,y):
    if(ga[2*x+1][4*y+1]=="X"):
      return -1
    return 1
  
  def explosion(self):
		x = bps[0]
		y = bps[1]
		self.de(x,y)
		self.ae(x,y)

		if(self.cp(x-1,y)>0):
			self.de(x-1,y)
			self.ae(x-1,y)

		if(self.cp(x+1,y)>0):
			self.de(x+1,y)
			self.ae(x+1,y)

		if(self.cp(x,y-1)>0):
			self.de(x,y-1)
			self.ae(x,y-1)

		if(self.cp(x,y+1)>0):
			self.de(x,y+1)
			self.ae(x,y+1)
		return

