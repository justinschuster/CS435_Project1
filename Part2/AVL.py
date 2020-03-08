import Node 

class AVL:
	def __init__(self):
		self.root = Node.Node()
		self.root.left = Node.Node()
		self.root.right = Node.Node()

	# rebalance at a node violating the rank rule
	def rebalanceAVL(self, node):
		# INPUT: A node, v, where an imbalance may have occured in an AVL tree T
		# OUTPUT: An update of T to now be balanced 

		# v.height <= 1 + max(v.leftChild().height, v.rightChild.height())
		if node.left is not None and node.right is not None: 
		# TODO: Don't think this is completely right 
			node.height = 1 + max(node.left.height, node.right.height)

		# while v is not the root of T do
		while (node != self.root):
			# v <= v.parent()
			node = node.parent

			if node is None:
				return 

			# if |v.leftChild.height() - v.rightChild.height| > 1 then
			if node.left is not None and node.right is not None:
				if  (abs(node.left.height - node.right.height) > 1):
					# Let y be the tallest child of v 
					if (node.left.height > node.right.height):
						y = node.left
					else:
						y = node.right
					
					# and let x be the tallest child of y
					if (y.left.height > y.right.height):
						x = node.left
					else:
						x = node.right 

					# v <= restructure(x) (trinode restructure operation)
					if x.left is not None and x.right is not None: # need to find correct answer for 1 
						if ((x.left.height - x.right.height) > 1):
							node = self.rightRotate(x)
						elif ((x.right.height - x.left.height) > 1):
							node = self.leftRotate(x)

			# v.height <= 1 + max(v.leftChild.height, v.rightChild.height)
			if node.left is not None and node.right is not None:
				node.height = 1 + max(node.left.height, node.right.height)
			elif node.left is not None:
				node.height = 1 + node.left.height
			elif node.right is not None:
				node.height = 1 + node.right.height

		return

	# inserts node into AVL tree (iterative)
	def insertIter(self, key):
		# didnt add val yet because might not need it, just working with integers
		# they can be the key and the value

		# INPUT: a key-element pair, (key, val) and an AVL tree, self
		# OUTPUT: an update of T to now contain the item (key, val)

		# v <= IterativeTreeSearch(key, Tree (self)) V IS NOT VALUE 
		currNode = self.searchIter(key)	

		# if v is not an external node then
		if (currNode.height != 1): # I think height = 0 means external 
			# return "An item with key k is already in T"
			print("key %d is already in the AVL tree"% (key))
			return

		# Exapnd v into an internal node with two external-node children	
		currNode.key = key # v.key <= key  
		# v.value <= val 
		currNode.height = 1 # v.height <= 1

		# rebalanceAVL(val, Tree)
		self.rebalanceAVL(currNode)

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
		print("Inserting: %d"% (key))
		# get currentNode
		currNode = self.root
		parent = None 

		# while currNode != Null
		while currNode is not None:
		#	if currNode.key is not None:
		#		print("currNode.key: %d"% (currNode.key))
		#	else:
		#		print("currNode.key is null")

		#	if parent is not None:
		#		print("parent.key: %d"% (parent.key))
		#	else:
		#		print("parent is null")

			# base case 
			if currNode.key is None:
				currNode.key = key
				currNode.height = 1 # always expand exterior nodes
				currNode.parent = parent
		#		print("Inserted %d"% (key))
				return currNode 

			# (if) check the key with node key 
			if (currNode.key == key):
				# return the node if they're the same
				return currNode	
			elif (currNode.key > key): # if key to insert is left than node key 
				# currNode <= curr.left
				parent = currNode
				currNode = currNode.left 
				parent.left = currNode
			else: # if greater
				parent = currNode
				currNode = currNode.right # curr <= curr.right  
				parent.right = currNode

			print()

		#print("currNode is null")
		#if parent is not None:
		#	if parent.key is not None:
		#		print("parent.key: %d"% (parent.key))
		#	else:
		#		print("parent.key is null")

		#	if parent.left is not None and parent.left.key is not None:	
		#		print("parent.left: %d"% (parent.left.key))
		#	elif parent.right is not None and parent.right.key is not None:
		#		print("parent.right: %d"% (parent.right.key))
		#	else:
		#		print("Parent has no children")
		#else:
		#	print("parent is null")

		# create the new node
		currNode = Node.Node(key, 1, parent)
		currNode.left = Node.Node()
		currNode.right = Node.Node()

		# assign our new node to the proper child of the parent node
		if parent is not None and parent.key is not None:
			if currNode.key < parent.key:
				parent.left = currNode
			elif currNode.key > parent.key:
				parent.right = currNode

		currNode = Node.Node(key, 1, parent)
		currNode.left = Node.Node()
		currNode.right = Node.Node()

		return currNode

	# opposite direction of right rotate
	def leftRotate(self, node):
		oldRoot = node
		node = node.right
		node = oldRoot
		return node

	# rotate subtree's root's left child to become new root of subtree
	# old root is man the new root's right child
	def rightRotate(self, node):
		oldRoot = node
		node = node.left
		node.right = oldRoot
		return node


