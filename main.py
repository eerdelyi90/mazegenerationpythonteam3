import os
import random
from time import sleep


SIZEX = 30
SIZEY = 30
DIRECTIONS = [[0,1],[1,0],[-1,0],[0,-1]]
STEPS = 200


class MazeMatrix:
    def __init__(self, sizex, sizey):
        self.matrix = [[0 for x in range(SIZEX)] for y in range(SIZEY)] 
        self.nodeList = []

    def runMaze(self, currentstep, currentNode):        
        if (currentstep < STEPS ):
            currentstep = currentstep + 1
            if (len(self.nodeList) <= 0):
                currentNode = MazeNode(0,0,None,self)
                self.nodeList.append(currentNode)
            
            if(currentNode.hasNoOptions()):
                currentNode = currentNode.previousMazeNode
            else:
                currentNode.setMazeValue(True)
                # display current state of maze
                _ = os.system("clear")
                display_grid(self.matrix)
                sleep(0.08)

                nextNode = currentNode.createNextMazeNode()
                currentNode = nextNode
                self.nodeList.append(currentNode)
                self.runMaze(currentstep, currentNode)
        else:
            return


class MazeNode:
    value = False
    def __init__(self,x,y,previousMazeNode, maze):
        self.x = x
        self.y = y
        self.previousMazeNode = previousMazeNode

    def setMazeValue(self, value):
        maze.matrix[self.x][self.y] = value

    def hasNoOptions(self):
        return False

    def createNextMazeNode(self):
        nextNode = None
        rand = random.randrange(4)
        nextCoords = DIRECTIONS[rand]
        x_new, y_new = (self.x + nextCoords[0], self.y + nextCoords[1])
        if not in_grid(x_new, y_new):
            nextNode = self.createNextMazeNode()
        else: 
            nextNode = MazeNode(x_new, y_new, self, None)
        return nextNode


# helper functions
def display_line(line):
    print(
        ''.join((" " if cell is True else "x" for cell in line))
    )

def display_grid(grid):
    for line in grid:
        display_line(line)

def in_grid(x, y):
    return 0 <= x < SIZEX and 0 <= y < SIZEY


maze = MazeMatrix(SIZEX, SIZEY)
maze.runMaze(0,None)