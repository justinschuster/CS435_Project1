#	Justin Schuster
#	CS435-004
#	Project 1
#	BST methods implementation

from BST import BST
from Node import Node

# helper function to print out preorder traversal for testing
def printPreorder(root: Node, visited: []) -> None:
	if root is None or root.data is None:
		return

	print(root.data)
	visited.append(root.data)

	if (root.left is not None and root.right not in visited):
		printPreorder(root.left, visited)
	if (root.right is not None and root.right not in visited):	
		printPreorder(root.right, visited)
	return 

# deletes Node in BST recursively
def deleteRec(root, data):
	if data < root.data:
		print("going left")
		root.left = deleteRec(root.left, data)	
	elif data > root.data:
		root.right = deleteRec(root.right, data)
	elif data == root.data:
		if root.left is None and root.right is None: # Node to delete is a leaf
			root = None
			return root
		elif root.left is not None and root.right is None: # 1 child
			childNode = root.left
			root = childNode
			return root
		elif root.left is None and root.right is not None: # only right child exits
			childNode = root.right
			root = childNode
			return root

		temp = root.right.findMinRec() 
		root.data = temp.data
		root.right = deleteRec(root.right, temp.data)

	return root


def main() -> None:
	currTree = BST()
	currTree.insertRec(5)	
	currTree.insertRec(4)
	currTree.insertRec(3)
	currTree.insertRec(6)

	#minNode = currTree.root.findMinRec()
	#print(minNode.data)
	deleteRec(currTree.root, 4)



	#currTree.deleteIter(2)
	#currTree.insertIter(1)

	print("\nPreorder Traversal:")
	visited = []
	printPreorder(currTree.root, visited)

if __name__ == "__main__":
	main()