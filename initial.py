import numpy as np  

from numpy import ma


class robot:
                
    def __init__(self,x_initial,y_initial,orient_inital):
        self.maze=np.full((16,16),0) #Used for storing wall configuration.

        self.flood = np.full((16,16),255) #Used for storing the flood array and the costs which shall be used for traversal.
        
        self.x=x_initial  #Stores the location of x coordinate currently robot is at.
        self.y=y_initial  #Stores the location of y coordinate currently robot is at.

        self.orient = orient_inital #Stores orientation for the robot. 0 for north,1 for east, 2 for south and 3 for west.
        

    def isValid (self,y,x):
    #Checks if the given coordinates are valid ones.
        if(y>=0 and y<16 and x<16 and x>=0):
            return True 
        return False


    def flood_initial(self):  # For generating the initial flooded self.maze assuming no walls are present.

   
        self.flood[7][7] =0 #Destination Cells are given weightage as zero.
        self.flood[7][8] =0 
        self.flood[8][7] =0
        self.flood[8][8] =0


        for i in range(16):
            for j in range(16):
                xdist = min(abs(j-7),np.abs(j-8))
                ydist = min(abs(i-7),np.abs(i-8))
                self.flood[i][j] = xdist + ydist
        

    def isEnd(self): #Checks if the bot has reached the destination.
        if(self.self.maze[self.y][self.x]==0):
            return True
        else:
            return False 
        #Need to add the functionality for storing the path in memory.
        #If this returns true then we have to start the fast run.

    def giveSurroundings(self):
        #Returns the four neighbouring cells for a particular cell.


        y0,x0 = self.y+1,self.x #Cell at absolute north.
        y1,x1 = self.y,self.x+1 #Cell at absolute east.
        y2,x2 = self.y-1,self.x #Cell at absolute south.
        y3,x3 = self.y,self.x+1 #Cell at absolute west.

        return ((y0,x0),(y1,x1),(y2,x2),(y3,x3))
    
    def updateWalls(self,L,R,F):
        #Gives the wall the configuration based on the presence of walls on left, right or front of the robot.
        if(L and R and F):
            if (self.orient==0): 
                self.maze[self.y][self.x]= 13
            elif (self.orient==1): 
                self.maze[self.y][self.x]= 12
            elif (self.orient==2): 
                self.maze[self.y][self.x]= 11
            elif (self.orient==3): 
                self.maze[self.y][self.x]= 14

        elif (L and R and not F):
            if (self.orient==0 or self.orient== 2): 
                self.maze[self.y][self.x]= 9
            elif (self.orient==1 or self.orient==3): 
                self.maze[self.y][self.x]= 10

        elif (L and F and not R):
            if (self.orient==0): 
                self.maze[self.y][self.x]= 8
            elif (self.orient==1): 
                self.maze[self.y][self.x]= 7
            elif (self.orient==2): 
                self.maze[self.y][self.x]= 6
            elif (self.orient==3): 
                self.maze[self.y][self.x]= 5

        elif (R and F and not L):
            if (self.orient==0): 
                self.maze[self.y][self.x]= 7
            elif (self.orient==1): 
                self.maze[self.y][self.x]= 6
            elif (self.orient==2): 
                self.maze[self.y][self.x]= 5
            elif (self.orient==3): 
                self.maze[self.y][self.x]= 8

        elif(F):
            if (self.orient==0): 
                self.maze[self.y][self.x]= 2
            elif (self.orient==1): 
                self.maze[self.y][self.x]= 3
            elif (self.orient==2): 
                self.maze[self.y][self.x]= 4
            elif (self.orient==3): 
                self.maze[self.y][self.x]= 1

        elif(L):
            if (self.orient==0): 
                self.maze[self.y][self.x]= 1
            elif (self.orient==1): 
                self.maze[self.y][self.x]= 2
            elif (self.orient==2): 
                self.maze[self.y][self.x]= 3
            elif (self.orient==3): 
                self.maze[self.y][self.x]= 4

        elif(R):
            if (self.orient==0): 
                self.maze[self.y][self.x]= 3
            elif (self.orient==1): 
                self.maze[self.y][self.x]= 4
            elif (self.orient==2): 
                self.maze[self.y][self.x]= 1
            elif (self.orient==3): 
                self.maze[self.y][self.x]= 2

    def isAccessible(self,x1,y1):
    #Returns True if mouse can move to x1,y1 from x,y (it's current position).
        if (self.x==x1):
            if(self.y>y1):
                if(self.self.maze[self.y][self.x]==4 or self.maze[self.y][self.x]==5 or self.maze[self.y][self.x]==6 or 
                self.maze[self.y][self.x]==10 or self.maze[self.y][self.x]==11 or self.maze[self.y][self.x]==12 or self.maze[self.y][self.x]==14 ):
                    return (False)
                else:
                    return(True)
            else:
                if(self.maze[self.y][self.x]==2 or self.maze[self.y][self.x]==7 or self.maze[self.y][self.x]==8 or self.maze[self.y][self.x]==10 or 
                self.maze[self.y][self.x]==12 or self.maze[self.y][self.x]==13 or self.maze[self.y][self.x]==14 ):
                    return (False)
                else:
                    return(True)
            
        elif (self.y==y1):
            if(self.x>x1):
                if(self.maze[self.y][self.x]==1 or self.maze[self.y][self.x]==5 or self.maze[self.y][self.x]==8 or 
                self.maze[self.y][self.x]==9 or self.maze[self.y][self.x]==11 or self.maze[self.y][self.x]==13 or self.maze[self.y][self.x]==14 ):
                    return (False)
                else:
                    return (True)
            else:
                if(self.maze[self.y][self.x]==3 or self.maze[self.y][self.x]==6 or self.maze[self.y][self.x]==7 or 
                self.maze[self.y][self.x]==9 or self.maze[self.y][self.x]==11 or self.maze[self.y][self.x]==12 or self.maze[self.y][self.x]==13 ):
                    return (False)
                else:
                    return (True)




mouse = robot(0,0,0)
mouse.flood_initial()
print(mouse.flood) 



