#	Justin Schuster
#	CS435-004
#	Project 1
#	BST methods implementation

import BST

def main():
	currTree = BST.BST()
	currTree.insertIter(currTree.root, 3)
	currTree.insertIter(currTree.root, 2)

	visited = []
	currTree.printBST(currTree.root, visited)

if __name__ == "__main__":
	main()