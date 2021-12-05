import numpy as np  

from numpy import ma



                
def isValid (y,x):
    #Checks if the given coordinates are valid ones.
    if(y>=0 and y<16 and x<16 and x>=0):
        return True 
    return False


def flood_initial(maze):  # For generating the initial flooded maze assuming no walls are present.

   

    maze[7][7] =0 #Destination Cells are given weightage as zero.
    maze[7][8] =0 
    maze[8][7] =0
    maze[8][8] =0


    for i in range(16):
        for j in range(16):
            xdist = min(abs(j-7),np.abs(j-8))
            ydist = min(abs(i-7),np.abs(i-8))
            maze[i][j] = xdist + ydist
    
    return maze


maze = np.full((16,16),255) #255 defines highest possible value and that the cell has not been 
                            # visited yet.

print(flood_initial(maze))

