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

    def getSurrounds(self):
        ''' returns x1,y1,x2,y2,x3,y3,x4,y4 the four surrounding square
        '''
        x=self.x 
        y=self.y
        x3= x-1
        y3=y
        x0=x
        y0=y+1
        x1=x+1
        y1=y
        x2=x
        y2=y-1
        if(x1>=16):
            x1=-1
        if(y0>=16):
            y0=-1
        return (x0,y0,x1,y1,x2,y2,x3,y3)  #order of cells- north,east,south,west
    
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
    
    def isConsistent(self):
        #returns True if the value of current square is one
        #   greater than the minumum value in an accessible neighbour.
        #   That is the mouse can go from the current cell to another neighbouring cell having less cost. 

    #One of the neighbouring cells should have value one less
    #than current cell so that mouse can move to it.

        x= self.x 
        y=self.y  
        flood = self.flood

        x0,y0,x1,y1,x2,y2,x3,y3 = self.getSurrounds(x,y)
        val= flood[y][x]  #Cost of current cell.
        minVals=[-1,-1,-1,-1] #Cost stays -1 if not accessible.
        if (x0>=0 and y0>=0):
            if (self.isAccessible(x,y,x0,y0)):
                minVals[0]=flood[y0][x0]
        if (x1>=0 and y1>=0):
            if (self.isAccessible(x,y,x1,y1)):
                minVals[1]=flood[y1][x1]
        if (x2>=0 and y2>=0):
            if (self.isAccessible(x,y,x2,y2)):
                minVals[2]=flood[y2][x2]
        if (x3>=0 and y3>=0):
            if (self.isAccessible(x,y,x3,y3)):
                minVals[3]=flood[y3][x3]

        for i in range(4):
            if minVals[i]== -1:
                pass
            elif minVals[i]== val+1 :
                pass
            elif minVals[i]== val-1 :
                return True
        
        return False
    

    def makeConsistent(self):

        x=self.x 
        y=self.y
        x0,y0,x1,y1,x2,y2,x3,y3 = self.getSurrounds(x,y)
        flood = self.flood

        val= flood[y][x]
        minVals=[-1,-1,-1,-1]
        if (x0>=0 and y0>=0):
            if (self.isAccessible(x,y,x0,y0)):
                minVals[0]=flood[y0][x0]
            
        if (x1>=0 and y1>=0):
            if (self.isAccessible(x,y,x1,y1)):
                minVals[1]=flood[y1][x1]
        
        if (x2>=0 and y2>=0):
            if (self.isAccessible(x,y,x2,y2)):
                minVals[2]=flood[y2][x2]
            
        if (x3>=0 and y3>=0):
            if (self.isAccessible(x,y,x3,y3)):
                minVals[3]=flood[y3][x3]
                

        for i in range(4):
            if minVals[i]== -1: #not accessible.
                minVals[i]= 1000 # Assigning a high cost.

        minVal= min(minVals) #finds the minimum cost of nearest accessible cell.
        flood[y][x]= minVal+1 #Updates the cost of present cell accordingly.
        

    def floodFill(self,xprev,yprev):
        #updates the flood matrix such that every square is consistent (current cell is x,y) i.e. each cell has a neighboring cell to which it can
        # go which has one less cost than the current cell. 

        x = self.x 
        y = self.y
        flood = self.flood 
        if not self.isConsistent(x,y):
            flood[y][x]= flood[yprev][xprev]+1

        #Previous Cells have coordinates xprev and yprev
            
        stack=[]
        stack.append(x)
        stack.append(y)

        x0,y0,x1,y1,x2,y2,x3,y3= self.getSurrounds(x,y)
        if(x0>=0 and y0>=0):
            if (self.isAccessible(x,y,x0,y0)):
                stack.append(x0)
                stack.append(y0)
        if(x1>=0 and y1>=0):
            if (self.isAccessible(x,y,x1,y1)):
                stack.append(x1)
                stack.append(y1)
        if(x2>=0 and y2>=0):
            if (self.isAccessible(x,y,x2,y2)):
                stack.append(x2)
                stack.append(y2)
        if(x3>=0 and y3>=0):
            if (self.isAccessible(x,y,x3,y3)):
                stack.append(x3)
                stack.append(y3)

        while (len(stack)!= 0):
            yrun= stack.pop()
            xrun= stack.pop()

            if self.isConsistent(xrun,yrun):
                pass
            else:
                self.makeConsistent(xrun,yrun)
                stack.append(xrun)
                stack.append(yrun)
                x0,y0,x1,y1,x2,y2,x3,y3= self.getSurrounds(xrun,yrun)
                if(x0>=0 and y0>=0):
                    if (self.isAccessible(xrun,yrun,x0,y0)):
                        stack.append(x0)
                        stack.append(y0)
                if(x1>=0 and y1>=0):
                    if (self.isAccessible(xrun,yrun,x1,y1)):
                        stack.append(x1)
                        stack.append(y1)
                if(x2>=0 and y2>=0):
                    if (self.isAccessible(xrun,yrun,x2,y2)):
                        stack.append(x2)
                        stack.append(y2)
                if(x3>=0 and y3>=0):
                    if (self.isAccessible(xrun,yrun,x3,y3)):
                        stack.append(x3)
                        stack.append(y3)




mouse = robot(0,0,0)
mouse.flood_initial()
print(mouse.flood) 



