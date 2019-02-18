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
      ga[2*x+1][4*y+4]=bps[2]
      ga[2*x+2][4*y+1]=bps[2]
      ga[2*x+2][4*y+2]=bps[2]
      ga[2*x+2][4*y+3]=bps[2]
      ga[2*x+2][4*y+4]=bps[2]
    bps[2]-=1
    if(bps[2]==-1):
      self.explosion()
    return
  
