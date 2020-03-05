class Node:
	def __init__(self, data=None):
		self.left = None
		self.right = None 
		self.data = data

	# finds the minimum Node value in the subtree (recursive)
	def findMinRec(self):
		currNode = self
		if currNode.left is None:
			return currNode 
		else:
			return currNode.left.findMinRec()

		
	# finds the minimum Node value in the subtree
	def findMinIter(self):
		currNode = self
		# while left child of current node is not null
		while currNode.left is not None:
			# currNode = left child 
			currNode = currNode.left
		# return the currNode when we have no more left children
		return currNode

	# finds the maximum Node value in the sub tree
	def findMaxIter(self):
		currNode = self
		# while right child isnt null
		while currNode.right is not None:
			# currNode = right child
			currNode = currNode.right
		# return the currNode when have have no more right children
		return currNode	

	# finds the max Node value in the subtree (recursive)
	def findMaxRec():
		return

	# inserts Node into BST (recursive version)
	def insertRec(self, data):
		root = self
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
				root.left.insertRec(data)	
			else: # larger number to the right
				if root.right is None:
					root.right = Node()
				root.right.insertRec(data)

	# deletes Node in BST recursively
	def deleteRec(self, data, prevNode = None):
		if data < self.data:
			print("going left")
			self.left.deleteRec(data, self)
			return
		elif data > self.data:
			self.right.deleteRec(data, self)
			return
		elif data == self.data:
			self = None 	
			if prevNode is not None:
				prevNode.left = self
			return