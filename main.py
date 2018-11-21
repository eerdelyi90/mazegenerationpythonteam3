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

class MazeNode:
	value = False
	def __init__(self,x,y,previousMazeNode,isCurrent):
		self.x = x
		self.y = y

	def setMazeValue(self, value):
		MazeMatrix[self.x][self.y] = value

    # def getRandomNextNode(self):
    #     moves = [(-1,0),(1,0),(0,-1),(0,1)]
    #     nextNode = moves[random.randrange(4)]



def display_line(line):
    print(
        ''.join(("o" if cell is True else "x" for cell in line))
    )

def display_grid(grid):
    for line in grid:
        display_line(line)


def in_grid(x, y):
    return 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE



firstNode = MazeNode(0, 0, None, True)
firstNode.setMazeValue(True)




display_grid(MazeMatrix)

# loop until done (PROBS A WHILE loop)
# if(mazeNodeList.length <= 0):
# 	currentNode = MazeNode(0,0,None,True)
# 	mazeNodeList.append(currentNode)

# #currentNode.setMazeValue()
# if(currentNode.hasNoOptions()):
# 	currentNode = currentNode.previousMazeNode

# print(MazeMatrix)

