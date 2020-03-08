import Node 

class AVL:
	def __init__(self):
		self.root = Node.Node()

	# rebalance at a node violating the rank rule
	def rebalanceAVL(self, value):
		# INPUT: A node, v, where an imbalance may have occured in an AVL tree T
		# OUTPUT: An update of T to now be balanced 
		# v.height <= 1 + max(v.leftChild().height, v.rightChild.height())
		# while v is not the root of T do
			# v <= v.parent()
			# if |v.leftChild.height() - v.rightChild.height| > 1 then 
				# Let y be the tallest child of v and let x be the tallest child of y
				# v <= restructure(x) (trinode restructure operation)
			# v.height <= 1 + max(v.leftChild.height, v.rightChild.height)
		return

	# inserts node into AVL tree (iterative)
	def insertIter(self, key):
		# didnt add val yet because might not need it, just working with integers
		# they can be the key and the value
		# INPUT: a key-element pair, (key, val) and an AVL tree, self
		# OUTPUT: an update of T to now contain the item (key, val)

		# v <= IterativeTreeSearch(key, Tree (self)) V IS NOT VALUE 
		# if v is not an external node then
			# return "An item with key k is already in T"
		# Exapnd v into an internal node with two external-node children
		# v.key <= key 
		# v.value <= val 
		# v.height <= 1
		# rebalanceAVL(val, Tree)
		return 

	# removes node from AVL tree 
	def deleteIter(self, key):
		# INPUT: a key, k and an AVL tree self
		# OUTPUT: an update of T to now have an item (key, value) removed 
		# v <= iterativeTreeSearch(self, key)
		# if v is an external node then:
			# return "There is not item with key k in T"
		# if v has no external-node child then
			# let u be the node in T with the key nearest to k
			# Move u's key-value to pair to v
			# v <= u
		# Let w be v's smallest-height child
		# Remove w and v from T, replacing v with w's sibling, z
		# rebalanceAVL(z, T)
		return 

	# searches AVL Tree self for the key then returns that node 
	# TODO: TEST THIS SHIT 
	def searchIter(self, key) -> Node:
		# get currentNode
		currNode = self.root

		# while currNode != Null
		while currNode is not None:
			# (if) check the key with node key 
			if (currNode.key == key):
				# return the node if they're the same
				return currNode	
			elif currNode.key > key: # if key to insert is left than node key 
				# currNode <= curr.left
				currNode = currNode.left
			else: # if greater
				currNode = currNode.right # curr <= curr.right 
		
		return currNode 


