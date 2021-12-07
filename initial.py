import numpy as np  

from numpy import ma



def isValid (y,x):
    #Checks if the given coordinates are valid ones.
        if(y>=0 and y<16 and x<16 and x>=0):
            return True 
        return False


def flood_initial():  # For generating the initial flooded maze assuming no walls are present.

        global flood

   
        flood[7][7] =0 #Destination cells are given weightage as zero.
        flood[7][8] =0 
        flood[8][7] =0
        flood[8][8] =0


        for i in range(16):
            for j in range(16):
                xdist = min(abs(j-7),np.abs(j-8))
                ydist = min(abs(i-7),np.abs(i-8))
                flood[i][j] = xdist + ydist
        

def isEnd(self): #Checks if the bot has reached the destination.
    if(maze[y][x]==0):
            return True
    else:
            return False 
    #Need to add the functionality for storing the path in memory.
    #If this returns true then we have to start the fast run.

def updateWalls(x,y,orient,L,R,F):

    global maze
    if(L and R and F):
        if (orient==0): 
            maze[y][x]= 13
        elif (orient==1): 
            maze[y][x]= 12
        elif (orient==2): 
            maze[y][x]= 11
        elif (orient==3): 
            maze[y][x]= 14

    elif (L and R and not F):
        if (orient==0 or orient== 2): 
            maze[y][x]= 9
        elif (orient==1 or orient==3): 
            maze[y][x]= 10

    elif (L and F and not R):
        if (orient==0): 
            maze[y][x]= 8
        elif (orient==1): 
            maze[y][x]= 7
        elif (orient==2): 
            maze[y][x]= 6
        elif (orient==3): 
            maze[y][x]= 5

    elif (R and F and not L):
        if (orient==0): 
            maze[y][x]= 7
        elif (orient==1): 
            maze[y][x]= 6
        elif (orient==2): 
            maze[y][x]= 5
        elif (orient==3): 
            maze[y][x]= 8

    elif(F):
        if (orient==0): 
            maze[y][x]= 2
        elif (orient==1): 
            maze[y][x]= 3
        elif (orient==2): 
            maze[y][x]= 4
        elif (orient==3): 
            maze[y][x]= 1

    elif(L):
        if (orient==0): 
            maze[y][x]= 1
        elif (orient==1): 
            maze[y][x]= 2
        elif (orient==2): 
            maze[y][x]= 3
        elif (orient==3): 
            maze[y][x]= 4

    elif(R):
        if (orient==0): 
            maze[y][x]= 3
        elif (orient==1): 
            maze[y][x]= 4
        elif (orient==2): 
            maze[y][x]= 1
        elif (orient==3): 
            maze[y][x]= 2
    
def isAccessible(x,y,x1,y1):
    #returns True if mouse can move to x1,y1 from x,y (two adjacent cells)

    global maze
    
    if (x==x1):
        if(y>y1):
            if(maze[y][x]==4 or maze[y][x]==5 or maze[y][x]==6 or maze[y][x]==10 or maze[y][x]==11 or maze[y][x]==12 or maze[y][x]==14 ):
                return (False)
            else:
                return(True)
        else:
            if(maze[y][x]==2 or maze[y][x]==7 or maze[y][x]==8 or maze[y][x]==10 or maze[y][x]==12 or maze[y][x]==13 or maze[y][x]==14 ):
                return (False)
            else:
                return(True)
            
    elif (y==y1):
        if(x>x1):
            if(maze[y][x]==1 or maze[y][x]==5 or maze[y][x]==8 or maze[y][x]==9 or maze[y][x]==11 or maze[y][x]==13 or maze[y][x]==14 ):
                return (False)
            else:
                return (True)
        else:
            if(maze[y][x]==3 or maze[y][x]==6 or maze[y][x]==7 or maze[y][x]==9 or maze[y][x]==11 or maze[y][x]==12 or maze[y][x]==13 ):
                return (False)
            else:
                return (True)

def getSurrounds(x,y):
    # Returns x1,y1,x2,y2,x3,y3,x4,y4 the four surrounding square
    
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

def isConsistent(x,y):

    global flood
    #returns True if the value of current square is one greater than the minumum value of an accessible neighbour.

    #One of the neighbouring cells should have value one less
    #than current cell so that mouse can move to it.

    x0,y0,x1,y1,x2,y2,x3,y3 = getSurrounds(x,y)
    val= flood[y][x]  #Cost of current cell.
    minVals=[-1,-1,-1,-1]
    if (x0>=0 and y0>=0):
        if (isAccessible(x,y,x0,y0)):
            minVals[0]=flood[y0][x0]
    if (x1>=0 and y1>=0):
        if (isAccessible(x,y,x1,y1)):
            minVals[1]=flood[y1][x1]
    if (x2>=0 and y2>=0):
        if (isAccessible(x,y,x2,y2)):
            minVals[2]=flood[y2][x2]
    if (x3>=0 and y3>=0):
        if (isAccessible(x,y,x3,y3)):
            minVals[3]=flood[y3][x3]

    for i in range(4):
        if minVals[i]== -1:
            pass
        elif minVals[i]== val+1 :
            pass
        elif minVals[i]== val-1 :
           return True
    
    return False

    

def makeConsistent(x,y):
    x0,y0,x1,y1,x2,y2,x3,y3 = getSurrounds(x,y)

    global flood

    #Makes the current cell consistent i.e there most be atleast one cell in the surroundings having cost one less than the present cell.

    val= flood[y][x]
    minVals=[-1,-1,-1,-1]
    if (x0>=0 and y0>=0):
        if (isAccessible(x,y,x0,y0)):
            minVals[0]=flood[y0][x0]
           
    if (x1>=0 and y1>=0):
        if (isAccessible(x,y,x1,y1)):
            minVals[1]=flood[y1][x1]
       
    if (x2>=0 and y2>=0):
        if (isAccessible(x,y,x2,y2)):
            minVals[2]=flood[y2][x2]
           
    if (x3>=0 and y3>=0):
        if (isAccessible(x,y,x3,y3)):
            minVals[3]=flood[y3][x3]
            

    for i in range(4):
        if minVals[i]== -1: #not accessible.
            minVals[i]= 1000 # Assigning a high cost.

    minVal= min(minVals) #finds the minimum cost of nearest accessible cell.
    flood[y][x]= minVal+1 #Updates the cost of present cell accordingly.

def floodFill(x,y,xprev,yprev):

    global flood 
    #Updates the flood matrix such that each and every cell is consistent. 
    if not isConsistent(x,y):
        flood[y][x]= flood[yprev][xprev]+1

    #Previous Cell is represented by xprev and yprev
        
    stack=[]
    stack.append(x)
    stack.append(y)
    x0,y0,x1,y1,x2,y2,x3,y3= getSurrounds(x,y)
    if(x0>=0 and y0>=0):
        if (isAccessible(x,y,x0,y0)):
            stack.append(x0)
            stack.append(y0)
    if(x1>=0 and y1>=0):
        if (isAccessible(x,y,x1,y1)):
            stack.append(x1)
            stack.append(y1)
    if(x2>=0 and y2>=0):
        if (isAccessible(x,y,x2,y2)):
            stack.append(x2)
            stack.append(y2)
    if(x3>=0 and y3>=0):
        if (isAccessible(x,y,x3,y3)):
            stack.append(x3)
            stack.append(y3)

    while (len(stack)!= 0):
        yrun= stack.pop()
        xrun= stack.pop()

        if isConsistent(xrun,yrun):
            pass
        else:
            makeConsistent(xrun,yrun)
            stack.append(xrun)
            stack.append(yrun)
            x0,y0,x1,y1,x2,y2,x3,y3= getSurrounds(xrun,yrun)
            if(x0>=0 and y0>=0):
                if (isAccessible(xrun,yrun,x0,y0)):
                    stack.append(x0)
                    stack.append(y0)
            if(x1>=0 and y1>=0):
                if (isAccessible(xrun,yrun,x1,y1)):
                    stack.append(x1)
                    stack.append(y1)
            if(x2>=0 and y2>=0):
                if (isAccessible(xrun,yrun,x2,y2)):
                    stack.append(x2)
                    stack.append(y2)
            if(x3>=0 and y3>=0):
                if (isAccessible(xrun,yrun,x3,y3)):
                    stack.append(x3)
                    stack.append(y3)

def toMove(x,y,xprev,yprev,orient):
    '''Returns the direction to turn into L,F,R or B
    '''
    global flood

    x0,y0,x1,y1,x2,y2,x3,y3 = getSurrounds(x,y)
    val= flood[y][x]
    prev=0 #Stores the cell from which we have come.

    minVals=[1000,1000,1000,1000]

    if (isAccessible(x,y,x0,y0)):
        if (x0==xprev and y0==yprev):
            prev=0
        minVals[0]= flood[y0][x0]

    if (isAccessible(x,y,x1,y1)):
        if (x1==xprev and y1==yprev):
            prev=1
        minVals[1]= flood[y1][x1]

    if (isAccessible(x,y,x2,y2)):
        if (x2==xprev and y2==yprev):
            prev=2
        minVals[2]= flood[y2][x2]

    if (isAccessible(x,y,x3,y3)):
        if (x3==xprev and y3==yprev):
            prev=3
        minVals[3]= flood[y3][x3]

    minVal=minVals[0] #Stores the minVal.
    minCell=0 # Stores the cell which has minimum cost.
    noMovements=0
    for i in minVals:
        if (i!=1000):
            noMovements+=1

    #noMovements=1 implies only one cell is accessible to it.

    for i in range(4):
        if (minVals[i]<minVal):
            if (noMovements==1): 
                minVal= minVals[i]
                minCell= i
            else:
                if(i==prev):
                    pass
                else:
                    minVal= minVals[i]
                    minCell= i

    if (minCell==orient):
        return ('F')
    elif((minCell==orient-1) or (minCell== orient+3)):
        return('L')
    elif ((minCell==orient+1) or (minCell== orient-3)):
        return('R')
    else:
        return('B')


    


def main():

    global x
    global y 
    global maze 
    global flood 
    global orient 
    
   

    xprev=0
    yprev=0  
    
    maze=np.full((16,16),0) #Used for storing wall configuration.

    flood = np.full((16,16),255) #Used for storing the flood array and the costs which shall be used for traversal.
        
    x=0  #Stores the location of x coordinate currently robot is at.
    y=0 #Stores the location of y coordinate currently robot is at.

    orient = 0 #(orient_inital) #Stores orientation for the robot. 0 for north,1 for east, 2 for south and 3 for west.

    flood_initial()
    print(flood) 
 


if __name__ == '__main__':
    maze =[] #Used for storing wall configuration.
    flood =[]#Used for storing the flood array and the costs which shall be used for traversal.       
    x=0#Stores the location of x coordinate currently robot is at.
    y=0 #Stores the location of y coordinate currently robot is at.
    orient=0#(orient_inital) #Stores orientation for the robot. 0 for north,1 for east, 2 for south and 3 for west.

    while True:

        L= api.wallLeft()
        R= api.wallRight()
        F= api.wallFront()
        updateWalls(x,y,orient,L,R,F)

        if (flood[y][x]!=0):
            floodFill(x,y,xprev,yprev)
        else:
            print("Eureka!! Path has been found")
            break
       
        direction= toMove(x,y,xprev,yprev,orient)

        
        if (direction=='L'):
            api.turnLeft()
            orient = api.orientation(orient,'L')

        elif (direction=='R'):
            api.turnRight()
            orient = api.orientation(orient,'R')

        elif (direction=='B'):
            api.turnLeft()
            orient = api.orientation(orient,'L')
            api.turnLeft()
            orient = api.orientation(orient,'L')


        log("moveForward")
        showFlood(x,y)
        api.moveForward()
        xprev=x
        yprev=y
        x,y = api.updateCoordinates(x,y,orient)
        

    main()




