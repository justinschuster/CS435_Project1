class Node:
	def __init__(self, key = None, height = 0, parent = None):
		self.key = key
		self.height = height 
		self.parent = parent
		self.left = None
		self.right = None 