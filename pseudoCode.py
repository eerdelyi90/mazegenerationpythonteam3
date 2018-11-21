import os
import random
from time import sleep
# hello init file

# WALL = 'o'
# Space = ' '
sizex = 8
sizey = 8
numberOfSteps = 25
directions = [[0,1],[1,0],[-1,0],[0,-1]]


MazeMatrix = [[0 for x in range(sizex)] for y in range(sizey)] 
mazeNodeList = []

class MazeNode:
	value = False
	def __init__(self,x,y,previousMazeNode,isCurrent):
		self.x = x
		self.y = y

	def setMazeValue():
		MazeMatrix[self.x][self.y] = value

	def hasNoOptions():
		#has no where to go



# loop until done (PROBS A WHILE loop)
for x in range(numberOfSteps):
	if (mazeNodeList.length <= 0):
		currentNode = MazeNode(0,0,None,True)
		mazeNodeList.append(currentNode)
	
	#currentNode.setMazeValue()
	if(currentNode.hasNoOptions()):
		currentNode = currentNode.previousMazeNode


	




