import os
import random
from time import sleep
# hello init file

# WALL = 'o'
# Space = ' '
sizex = 20
sizey = 20
MazeMatrix = [[0 for x in range(sizex)] for y in range(sizey)] 
mazeNodeList = []
directions = [[0,1],[1,0],[-1,0],[0,-1]]

currentstep = 0

numberOfSteps = 25


class MazeNode:
    value = False
    def __init__(self,x,y,previousMazeNode,isCurrent):
        self.x = x
        self.y = y
        self.previousMazeNode = previousMazeNode

    def setMazeValue(self, value):
        MazeMatrix[self.x][self.y] = value

    def hasNoOptions(self):
        return False

    def createNextMazeNode(self):
        nextNode = None
        rand = random.randrange(4)
        nextCoords = directions[rand]
        x_new = self.x + nextCoords[0]
        y_new = self.y + nextCoords[1]
        if not in_grid(x_new, y_new):
            nextNode = self.createNextMazeNode()
        else: 
            nextNode = MazeNode(x_new, y_new, self, None)
        return nextNode


def display_line(line):
    print(
        ''.join((" " if cell is True else "x" for cell in line))
    )

def display_grid(grid):
    for line in grid:
        display_line(line)


def in_grid(x, y):
    return 0 <= x < sizex and 0 <= y < sizey

firstNode = MazeNode(0, 0, None, True)
firstNode.setMazeValue(True)

# loop until done (PROBS A WHILE loop)

def runMaze():

    global currentstep
    global currentNode
    print(currentstep)
    if (currentstep < numberOfSteps ):
        currentstep = currentstep + 1
        if (len(mazeNodeList) <= 0):
            currentNode = MazeNode(0,0,None,True)
            mazeNodeList.append(currentNode)
        
        #currentNode.setMazeValue()
        if(currentNode.hasNoOptions()):
            currentNode = currentNode.previousMazeNode
        else:
            currentNode.setMazeValue(True)
            nextNode = currentNode.createNextMazeNode()
            currentNode = nextNode
            mazeNodeList.append(currentNode)
            runMaze()
    else:
        return
        #stop


runMaze()


# while True:
#     _ = os.system("clear")
#     grid = update_grid(grid)
#     display_grid(grid)
#     sleep(0.5)

display_grid(MazeMatrix)
