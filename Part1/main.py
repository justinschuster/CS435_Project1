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

# finds the next node inorder
def findNextRec(root, data, prevNode=None):
	if root is None:
		return None

	if root.data == data:
		if root.right is not None:
			return root.right.findMinRec()
	elif data < root.data:
		prevNode = root
		return findNextRec(root.left, data, prevNode)
	else:
		return findNextRec(root.right, data, prevNode)

	return prevNode


def main() -> None:
	currTree = BST()
	currTree.insertRec(15)	
	currTree.insertRec(10)
	currTree.insertRec(8)
	currTree.insertRec(12)
	currTree.insertRec(20)
	currTree.insertRec(16)
	currTree.insertRec(25)

	print(findNextRec(currTree.root, 8).data)

	#deleteRec(currTree.root, 4)

	#currTree.deleteIter(2)
	#currTree.insertIter(1)


	print("\nPreorder Traversal:")
	visited = []
	printPreorder(currTree.root, visited)

if __name__ == "__main__":
	main()