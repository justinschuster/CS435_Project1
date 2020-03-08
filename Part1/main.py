#	Justin Schuster
#	CS435-004
#	Project 1
#	BST methods implementation

from BST import BST
from Node import Node
from testing import TestMethods
import random 

# inserts Node into BST (recursive version)
def insertRec(root, data):
	if  root is None: # base case 
		root = Node(data)
	elif root.data is None:
		root.data = data
	else:
		if data == root.data:
			root.data = data 
		elif data < root.data: # smaller number to left child	
			if root.left is None:
				root.left = Node()
			insertRec(root.left, data)	
		else: # larger number to the right
			if root.right is None:
				root.right = Node()
			insertRec(root.right, data)

# deletes Node in BST recursively
def deleteRec(root, data):
	if data < root.data:
		print("going left")
		root.left = deleteRec(root.left, data)	
	elif data > root.data:
		root.right = deleteRec(root.right, data)
	elif data == root.data:
		if root.left is None and root.right is None: # Node to delete is a leaf
			root = None
			return root
		elif root.left is not None and root.right is None: # 1 child
			childNode = root.left
			root = childNode
			return root
		elif root.left is None and root.right is not None: # only right child exits
			childNode = root.right
			root = childNode
			return root

		temp = root.right.findMinRec() 
		root.data = temp.data
		root.right = deleteRec(root.right, temp.data)

	return root

# finds the next node inorder
def findNextRec(root, data, prevNode=None):
	if root is None:
		return None

	if root.data == data:
		if root.right is not None:
			return root.right.findMinRec()
	elif data < root.data:
		prevNode = root
		return findNextRec(root.left, data, prevNode)
	else:
		return findNextRec(root.right, data, prevNode)

	return prevNode

# finds the previous node inorder (recursive)
def findPrevRec(root, data, prevNode=None):
	if root is None:
		return prevNode

	if data == root.data:
		if root.left is not None:
			return root.left.findMaxRec()
	elif data < root.data:
		return findPrevRec(root.left, data, prevNode)
	else:
		prevNode = root
		return findPrevRec(root.right, data, prevNode)

	return prevNode

# finds next node inorder (iterative)
def findNextIter(root, data):
	prevNode = Node()

	while True:
		if data > root.data:
			root = root.right
		elif data < root.data:
			prevNode = root
			root = root.left
		else:
			if root.right is not None:
				prevNode = root.right.findMinIter()
			break

		if root is None:
			return None

	return prevNode 

# finds the previous node inoder (iterative)
def findPrevIter(root, data):
	prevNode = Node()

	while True:
		if data > root.data:
			prevNode = root 
			root = root.right
		elif data < root.data:
			root = root.left
		else:
			if root.left is not None:
				prevNode = root.left.findMaxIter();
			break

		if root is None:
			return None

	return prevNode

# finds the minimum Node value in the subtree (recursive)
def findMinRec(currNode):
	if currNode.left is None:
		return currNode 
	else:
		return currNode.left.findMinRec()

# finds the max Node value in the subtree (recursive)
def findMaxRec(currNode):
	if currNode.right is None:
		return currNode
	else:
		return currNode.right.findMaxRec()

# finds the minimum Node value in the subtree (recursive)
def findMinRec(currNode):
	if currNode.left is None:
		return currNode 
	else:
		return currNode.left.findMinRec()

# finds the max Node value in the subtree (recursive)
def findMaxRec(currNode):
	if currNode.right is None:
		return currNode
	else:
		return currNode.right.findMaxRec()

	
# finds the minimum Node value in the subtree
def findMinIter(currNode):
	# while left child of current node is not null
	while currNode.left is not None:
		# currNode = left child 
		currNode = currNode.left
	# return the currNode when we have no more left children
	return currNode

# finds the maximum Node value in the sub tree
def findMaxIter(currNode):
	# while right child isnt null
	while currNode.right is not None:
		# currNode = right child
		currNode = currNode.right
	# return the currNode when have have no more right children
	return currNode	

# inserts Node into BST (iterative version)
def insertIter(root, data: int) -> None:
	# Set currNode = root
	currNode = root 
	prevRight = None
	prevLeft = None

	# while currNode isn't null
	while (currNode != None):
		# if currData = data
		if (data == currNode.data or currNode.data is None):	
			currNode.data = data
			return

		# if data < currData 
		if (data < currNode.data):
			# currNode = left child of currnode 
			prevRight = None 
			prevLeft = currNode
			currNode = currNode.left	
		# if data > currData
		elif (data > currNode.data):
			prevLeft = None
			prevRight = currNode
			currNode = currNode.right

	currNode = Node(data)
	if (prevRight):
		prevRight.right = currNode
	elif (prevLeft):
		prevLeft.left = currNode


# deletes Node from BST (iterative version)
def deleteIter(root, deleteValue: int) -> None:
	prevNode = None # set prevNode = none
	currNode =  root # set currNode = root 

	# if root is null
	if  currNode is None:
		# return 
		return

	# while currNode is not null
	while currNode is not None:
		# if currNode value is equal to the value we want to delete -> delete
		if (currNode.data == deleteValue == prevNode.left.data):
			# node to delete has no children
			if (currNode.right == currNode.left == None):
				prevNode.left = None
				break
			# node to delete only has right child
			elif (currNode.right is not None and currNode.left is None):
				prevNode.left = currNode.right
				break
			elif (currNode.right is None and currNode is not None):
				prevNode.left = currNode.left
				break

		prevNode = currNode # prevNode = current node  
		# if delete value is less that data of current
		if (currNode.data > deleteValue):
			# make currNode into currNode's left child
			currNode = currNode.left
		# otherwise make currNode into currNodes right child
		else:
			currNode = currNode.right 
	return

# creates an array of size n that contains distinct random numbers
def getRandomArray(n) -> []:
	# count and array 
	arr = [] 
	count = 0

	# loop n times, only iterate count if we insert number 
	while (count < n):
		newNum = random.randint(0, 200)	
		if arr.count(newNum) == 0:
			arr.append(newNum)	
			count = count + 1

	return arr

	
def main() -> None:
	#treeNodes = [5, 4, 7, 1, 9]

	#currTree = BST()
	#for n in treeNodes:
		#insertRec(currTree.root, n)

	#TestMethods.testInsert(currTree.root)

	arr = getRandomArray(10)
	for num in arr:
		print(num)


if __name__ == "__main__":
	main()