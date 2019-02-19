
ga=[[0 for x in range(20)] for y in range(30) ]
class board():
    def gameboard(self):
        ga[0][0]=1
        for i in range(1,19):
            for j in range(1,29):
                if (i<3 or i>17):
                    ga[i][j]="X"
                elif (j<4 or j>26):
                    ga[i][j]="X"
                elif((i>4 and i<17 and j<27 and j>8) and (i%4==1 or i%4==2)and (j%8==1 or j%8==2 or j%8==3 or j%8==4)):
                    ga[i][j]="X"
                else:
                    ga[i][j]="0"
                
                
        return ga        
