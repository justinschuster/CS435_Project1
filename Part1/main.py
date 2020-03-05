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


def main() -> None:
	currTree = BST()
	currTree.insertRec(5)	
	currTree.insertRec(4)
	#currTree.insertIter(3)

	#currTree.deleteIter(2)
	#currTree.insertIter(1)

	print("\nPreorder Traversal:")
	visited = []
	printPreorder(currTree.root, visited)

if __name__ == "__main__":
	main()