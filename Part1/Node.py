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

	# finds the max Node value in the subtree (recursive)
	def findMaxRec(self):
		currNode = self
		if currNode.right is None:
			return currNode
		else:
			return currNode.right.findMaxRec()

		
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
def deleteRec(self, data):
	if data < self.data:
		print("going left")
		return self.left.deleteRec(data)	
	elif data > self.data:
		return self.right.deleteRec(data)
	elif data == self.data:
		if self.left is None and self.right is None: # Node to delete is a leaf
			self = None
			return self
		elif self.left is not None and self.right is None: # 1 child
			childNode = self.left
			self = childNode
			return self
		elif self.left is None and self.right is not None: # only right child exits
			childNode = self.right
			self = childNode
			return self

		temp = self.right.findMinRec() 
		self.data = temp.data
		self.right = self.right.deleteRec(temp.data)