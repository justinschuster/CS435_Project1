import Node
import AVL 

# help testing, prints Inorder traversal
def printInorder(node):
	
	if node.left is not None and node.left.key is not None:
		printInorder(node.left)

	print(node.key, end=" ")

	if node.right is not None and node.right.key is not None: 
		printInorder(node.right)

# check to see if it is a valid AVL tree (rank rule and all  that jazz)
def isValidAVL(node):
	# check if node is null
	if node is None or node.key is None:
		return True

	# check if node has child nodes
	if node.left is not None and node.left.key is not None:
		if node.right is not None and node.right.key is not None:
			rank = abs(node.left.height - node.right.height) 
			if (rank > 1):
				print("Not a valid AVL tree")
				print("node.left.key: %d, node.right.key: %d"% (node.left.key, node.right.key))
				print("node.left.height: %d, node.right.height: %d, rank: %d"%
						(node.left.height, node.right.height, rank))
				return False
	
	return isValidAVL(node.left) and isValidAVL(node.right)




