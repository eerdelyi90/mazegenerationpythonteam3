import os
import random
from time import sleep
# hello init file

# WALL = 'o'
# Space = ' '
sizex = 8
sizey = 8
numberOfSteps = 25
currenstep = 0
directions = [[0,1],[1,0],[-1,0],[0,-1]]


MazeMatrix = [[0 for x in range(sizex)] for y in range(sizey)] 
mazeNodeList = []

class MazeNode:
	nextNode = None
	def __init__(self,x,y,previousMazeNode,isCurrent):
		self.x = x
		self.y = y

	def setMazeValue(value):
		MazeMatrix[self.x][self.y] = value

	def hasNoOptions():
		#has no where to go

	def createNextMazeNode():
		#pick a direction
		#create next node
		#return nextnode 






# loop until done (PROBS A WHILE loop)
def runMaze():
	if (currenstep < numberOfSteps ):
		currenstep++
		if (mazeNodeList.length <= 0):
			currentNode = MazeNode(0,0,None,True)
			mazeNodeList.append(currentNode)
		
		#currentNode.setMazeValue()
		if(currentNode.hasNoOptions()):
			currentNode = currentNode.previousMazeNode
		else:
			currentNode.setMazeValue(True)
			nextNode = currentNode.createNextMazeNode()
			currentNode = nextnode
			mazeNodeList.append(currentNode)
			runMaze()
	else:
		#stop







	




