#	Justin Schuster
#	CS435-004
#	Project 1
#	BST methods implementation

import BST

def main():
	currTree = BST.BST()
	currTree.insertIter(currTree.root, 1)
	currTree.insertIter(currTree.root, 5)	
	currTree.insertIter(currTree.root, 4)
	currTree.insertIter(currTree.root, 3)

	print(currTree.root.data)
	print(currTree.root.right.data)
	print(currTree.root.right.left.data)
	print(currTree.root.right.left.left.data)

	#currTree.deleteIter(2)

	visited = []
	#currTree.root.preOrder(visited)

if __name__ == "__main__":
	main()