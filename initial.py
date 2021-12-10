import numpy as np  

from numpy import ma



def isValid (y,x):
    #Checks if the given coordinates are valid ones.
        if(y>=0 and y<16 and x<16 and x>=0):
            return True 
        return False


def flood_initial():  # For generating the initial flooded maze assuming no walls are present.

        global flood

   
        flood[2][3] =0 #Destination cells are given weightage as zero.
        flood[3][3] =0 
        flood[3][2] =0
        flood[2][2] =0


        for i in range(6):
            for j in range(6):
                xdist = min(abs(j-2),abs(j-3))
                ydist = min(abs(i-2),abs(i-3))
                flood[i][j] = xdist + ydist
        

def isEnd(self): #Checks if the bot has reached the destination.
    if(maze[y][x]==0):
            return True
    else:
            return False 
    #Need to add the functionality for storing the path in memory.
    #If this returns true then we have to start the fast run.

    
def isAccessible(x,y,x1,y1):
    #returns True if mouse can move to x1,y1 from x,y (two adjacent cells)

    global maze

    if(x==x1 and y==y1):
        return False
    
    # if((x==0) and y==5 and y1==4 and x1==0):
    #     return True
    
    # if ((x==5) and y==0 and x1==5 and y1==1):
    #     return True

    # if ((x==5) and y==0 and x1==4 and y1==0):
    #     return True

    if (x==x1):
        if(y<y1):
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
    y0=y-1
    x1=x+1
    y1=y
    x2=x
    y2=y+1
    if(x1>=6):
        x1=5
    if(y0<0):                        #If overshooting values returning same cell value.
        y0=0
    if(x3<0):
        x3=0
    if(y2>=6):
        y2=5
    return (x0,y0,x1,y1,x2,y2,x3,y3)  #order of cells- north,east,south,west

def updateWalls(x,y,orient):

    L= int(input("Enter value for left "))
    R= int(input("Enter value for right "))
    F= int(input("Enter value for front "))

    global maze
    if(L==1 and R==1 and F==1):
        if (orient==0): 
            maze[y][x]= 13
        elif (orient==1): 
            maze[y][x]= 12
        elif (orient==2): 
            maze[y][x]= 11
        elif (orient==3): 
            maze[y][x]= 14

    elif (L==1 and R==1 and not F==1):
        if (orient==0 or orient== 2): 
            maze[y][x]= 9
        elif (orient==1 or orient==3): 
            maze[y][x]= 10

    elif (L==1 and F==1 and not R==1):
        if (orient==0): 
            maze[y][x]= 8
        elif (orient==1): 
            maze[y][x]= 7
        elif (orient==2): 
            maze[y][x]= 6
        elif (orient==3): 
            maze[y][x]= 5

    elif (R==1 and F==1 and not L==1):
        if (orient==0): 
            maze[y][x]= 7
        elif (orient==1): 
            maze[y][x]= 6
        elif (orient==2): 
            maze[y][x]= 5
        elif (orient==3): 
            maze[y][x]= 8

    elif(F==1):
        if (orient==0): 
            maze[y][x]= 2
        elif (orient==1): 
            maze[y][x]= 3
        elif (orient==2): 
            maze[y][x]= 4
        elif (orient==3): 
            maze[y][x]= 1

    elif(L==1):
        if (orient==0): 
            maze[y][x]= 1
        elif (orient==1): 
            maze[y][x]= 2
        elif (orient==2): 
            maze[y][x]= 3
        elif (orient==3): 
            maze[y][x]= 4

    elif(R==1):
        if (orient==0): 
            maze[y][x]= 3
        elif (orient==1): 
            maze[y][x]= 4
        elif (orient==2): 
            maze[y][x]= 1
        elif (orient==3): 
            maze[y][x]= 2
                                        

def isConsistent(x,y):

    global flood

    if(flood[y][x]==0):
        return True
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

    if(flood[y][x]==0):
        return None


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
    # if(y==5 and x==0):
    #     flood[y][x]=flood[4][0]+1
    # else:
    flood[y][x]= minVal+1 #Updates the cost of present cell accordingly.

def floodFill(x,y,xprev,yprev):

    global flood 
    #Updates the flood matrix such that each and every cell is consistent. 

    if(flood[y][x]==0):
        return None

    if not isConsistent(x,y):
        makeConsistent(x,y)

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
        xrun= stack.pop() #May have to change

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
def isChannel(x,y):
    global maze 
    return (maze[y][x]==9 or maze[y][x]==10) #Checks if the present cell is a channel.

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

    #noMovements=1 implies only one cell is accessible to it which is the previous cell.



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
    
    k = 0 # Counter for storing number of elements having the same minimum cost. 
    k = minVals.count(minVal) 
    #or (k>1 and minVals.count(minVals[orient])>1)


    if(minCell==orient ):
            return ('F')
    elif((minCell==orient-1) or (minCell== orient+3)):
            return('L')
    elif ((minCell==orient+1) or (minCell== orient-3)):
            return('R')
    else:
        return('B')

def updateCoordinates():

    global x
    global y
    global orient

    if (orient==0):
        y-=1
    if (orient==1):
        x+=1
    if (orient==2):
        y+=1
    if (orient==3):
        x-=1
        

def moveAndUpdate(direction):
    global x 
    global y
    global orient 
    global xprev
    global yprev

    if (direction=='L'):
            orient-=1 

    elif (direction=='R'):
            orient+=1

    elif (direction=='B'):
            orient+=2

    orient%=4

    xprev=x
    yprev=y
    updateCoordinates()

    print("X Coordinate ",x)
    print("Y Coordinate ",y)
    print(maze)
    print(flood)

def pruneHistory():

    global x
    global y

    findCell = [x,y]
    global historyCount
    global history
    
    #findCell represents the element of the dictionary. It is a tuple.
    i = historyCount -2 
    while(i>=0):
        cell = history[i] 
        if(cell[0] == findCell[0] and cell[1]==findCell[1]):
            historyCount = i+1 # May have to change later.
            return None
        i-=1

def addToHistory():
    #Stores the x,y and orientation of the robot at the particular cell.
    global x
    global y 
    global orient
    global historyCount
    global history
    
    history[historyCount] = (x,y,orient) 
    print(history)
    historyCount+=1 

    return None


def fastRun(): 

    global flood
    global walkCount
    global historyCount
    global orient

    while True:

        orient = history[walkCount][2] 
        moveForward_update()
        walkCount+=1 

        if(walkCount==historyCount):
            print("Fast Run Executed. Reached Destination")
            exit()
            # goHome()
            # break

def moveForward_update():
    global orient
    global x
    global y

    if(orient==0):
        y-=1
    elif(orient==1):
        x+=1
    elif(orient==2):
        y+=1
    else:
        x-=1
    
    print("X Coordinate is ", x)
    print("Y Coordinate is ",y)


    
def goHome():

   global walkCount
   global orient

   while True:
    walkCount-=1 

    orient = (history[walkCount][2]+2)%4 #Orientation should be just reverse of original run.
    #Now it needs to just move one block ahead.
    moveForward_update()

    if walkCount==0:
       print("Reached Home")
       fastRun() #Implement Fast Run. Breaks this.
       break

def main():

    global x
    global y 
    global maze 
    global flood 
    global orient 
    global xprev
    global yprev
    global historyCount 
    global history 
    global walkCount
    
   

    xprev=0
    yprev=5  
    
    # maze=np.full((16,16),0) #Used for storing wall configuration.

    flood = np.full((6,6),255) #Used for storing the flood array and the costs which shall be used for traversal.
    maze = np.full((6,6),0)
    maze[5][0]=11
        
    x=0  #Stores the location of x coordinate currently robot is at.
    y=5 #Stores the location of y coordinate currently robot is at.

    orient = 0 #(orient_inital) #Stores orientation for the robot. 0 for north,1 for east, 2 for south and 3 for west.

    flood_initial()
    print(flood) 

    while True:
            
        if (flood[y][x]!=0):
            if(maze[y][x]==0):
                updateWalls(x,y,orient)

            direction = toMove(x,y,xprev,yprev,orient)
            if(not isChannel(x,y)):
                if(not (x==0 and y==5)):
                    floodFill(x,y,xprev,yprev)
            moveAndUpdate(direction)
            addToHistory()
           
            pruneHistory()
            
            # Add Function for adding to history. Cross check once.

        else:

            print("Eureka!! Path has been found")
            walkCount=historyCount
            print(flood)
            print(historyCount)
            print()

            #Now it will go back.
            goHome()
           


     #Used for storing wall configuration.
maze = []
flood =[]#Used for storing the flood array and the costs which shall be used for traversal.       
x=0#Stores the location of x coordinate currently robot is at.
y=5 #Stores the location of y coordinate currently robot is at.
orient=0#(orient_inital) #Stores orientation for the robot. 0 for north,1 for east, 2 for south and 3 for west.
xprev =0
yprev =5


historyCount =0 #Stores the number of steps moved by the bot while reaching the destination.
history ={} #Dictionary that will store the co-ordinates and orientation of bot 
    #with co-ordinates as key and orientation as value.
walkCount =0 #TO store the number of cells to be moved while coming back.

main()