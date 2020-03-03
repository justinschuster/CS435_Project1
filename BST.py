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
				# currNode = rght child of currNode
				currNode = currNode.right 
		# currNode = new Node(data)
		currNode = Node.Node(data)

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
	def findMinIter(root: Node) -> Node:
		# currNode = root
		currNode = root 
		# while left child of current node is not null
		while currNode.leftChild is not None:
			# currNode = left child 
			currNode = currNode.left
		# return the currNode when we have no more left children
		return currNode

	# finds the maximum Node value in the BST
	def findMaxIter():
		return 

	def printBST(self, root: Node, visited: []) -> None:
		print(root.data)
		visited.append(root.data)
		if (root.left is not None and root.left not in visited):
			self.printBST(root.left, visited)
		if (root.right is not None and root.right not in visited):	
			self.printBST(root.right, visited)
		return 