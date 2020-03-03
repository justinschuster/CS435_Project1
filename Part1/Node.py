class Node:
	def __init__(self, data = None):
		self.data = data
		self.left = None
		self.right = None 

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


	def preOrder(self, visited: []) -> None:
		print(self.data)
		visited.append(self.data)
		if (self.left is not None and self.right not in visited):
			self.left.preOrder(visited)
		if (self.right is not None and self.right not in visited):	
			self.right.preOrder(visited)
		return 