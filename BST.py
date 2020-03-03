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
	def deleteIter():
		return

	# finds next Node in BST 
	def findNextIter():
		return

	# finds the previous Node in BST
	def findPrevIter():
		return

	# finds the minimum Node value in the subtree
	def findMinIter(self) -> Node:
		# currNode = root
		currNode = self.root 
		# while left child of current node is not null
		while currNode.left is not None:
			# currNode = left child 
			currNode = currNode.left
		# return the currNode when we have no more left children
		return currNode

	# finds the maximum Node value in the BST
	def findMaxIter(self):
		# currNode = root
		currNode = self.root
		# while right child isnt null
		while currNode.right is not None:
			# currNode = right child
			currNode = currNode.right
		# return the currNode when have have no more right children
		return currNode

	def printBST(self, root: Node, visited: []) -> None:
		print(root.data)
		visited.append(root.data)
		if (root.left is not None and root.left not in visited):
			self.printBST(root.left, visited)
		if (root.right is not None and root.right not in visited):	
			self.printBST(root.right, visited)
		return 