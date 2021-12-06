import numpy as np  

from numpy import ma


class robot:
                
    def __init__(self,x_initial,y_initial,orient_inital):
        self.maze=np.full((16,16),255) #255 defines highest possible value and that the cell has not been 
                            # visited yet.
        self.x=x_initial  #Stores the location of x coordinate currently robot is at.
        self.y=y_initial  #Stores the location of y coordinate currently robot is at.

        self.orient = orient_inital #Stores orientation for the robot. 0 for north,1 for east, 2 for south and 3 for west.


    def isValid (self,y,x):
    #Checks if the given coordinates are valid ones.
        if(y>=0 and y<16 and x<16 and x>=0):
            return True 
        return False


    def flood_initial(self):  # For generating the initial flooded maze assuming no walls are present.

   
        self.maze[7][7] =0 #Destination Cells are given weightage as zero.
        self.maze[7][8] =0 
        self.maze[8][7] =0
        self.maze[8][8] =0


        for i in range(16):
            for j in range(16):
                xdist = min(abs(j-7),np.abs(j-8))
                ydist = min(abs(i-7),np.abs(i-8))
                self.maze[i][j] = xdist + ydist
        

    def isEnd(self): #Checks if the bot has reached the destination.
        if(self.maze[self.y][self.x]==0):
            return True
        else:
            return False 
        #Need to add the functionality for storing the path in memory.

    def giveSurroundings(self):
        #Returns the four neighbouring cells for a particular cell.


        y0,x0 = self.y+1,self.x #Cell at absolute north.
        y1,x1 = self.y,self.x+1 #Cell at absolute east.
        y2,x2 = self.y-1,self.x #Cell at absolute south.
        y3,x3 = self.y,self.x+1 #Cell at absolute west.

        return ((y0,x0),(y1,x1),(y2,x2),(y3,x3))







