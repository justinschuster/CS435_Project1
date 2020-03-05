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

	# finds the minimum Node value in the subtree (recursive)
	def findMinRec():
		return

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
