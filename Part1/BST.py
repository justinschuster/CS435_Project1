import Node

class BST:
	def __init__(self) -> None:
		self.root = Node.Node()

	# inserts Node into BST
	def insertIter(self, root: Node, data: int) -> None:
		# Set currNode = root
		currNode = root
		# while currNode isn't null
		while currNode is not None:
			# currData = data of the currNode
			currData = currNode.data
			# if currData = data
			if (data == currData or currData == None):	
				currNode.data = data
				# return	
				return
			# if data < currData 
			if (data < currData):
				# currNode = left child of currnode 
				currNode.left = Node.Node(data)
				currNode = currNode.left
			# if data > currData
			elif (data > currData):
				# currNode = rght child Af currNode
				currNode.right = Node.Node(data)
				currNode = currNode.right 
		# currNode = new Node(data)
		# currNode = Node.Node(data)

	# deletes Node from BST
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

	# finds next Node in BST 
	def findNextIter():
		return

	# finds the previous Node in BST
	def findPrevIter():
		return
