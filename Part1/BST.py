import Node

class BST:
	def __init__(self) -> None:
		self.root = Node.Node()

	# inserts Node into BST (recursive version)
	def insertRec(self, data: int) -> None:
		return

	# inserts Node into BST (iterative version)
	def insertIter(self, data: int) -> None:
		# Set currNode = root
		currNode = self.root
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

		currNode = Node.Node(data)
		if (prevRight):
			prevRight.right = currNode
		elif (prevLeft):
			prevLeft.left = currNode


	# deletes Node from BST (iterative version)
	def deleteIter(self, deleteValue: int) -> None:
		prevNode = None # set prevNode = none
		currNode =  self.root # set currNode = root 

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

	# deletes Node from BST (recursive version)
	def deleteRec():
		return

	# finds next Node in BST 
	def findNextIter():
		return

	# finds next Node in BST (recursive)
	def findNextRec():
		return

	# finds the previous Node in BST
	def findPrevIter():
		return

	# finds the previous Node in the BST (recursive)
	def findPrevRec():
		return

	# helper function to print out preorder traversal for testing
	def printPreorder(self, root: Node, visited: []) -> None:
		print(root.data)
		visited.append(root.data)
		if (root.left is not None and root.right not in visited):
			self.printPreorder(root.left, visited)
		if (root.right is not None and root.right not in visited):	
			self.printPreorder(root.right, visited)
		return 
