#	Justin Schuster
#	CS435-004
#	Project 1
#	BST methods implementation

import BST

def main():
	currTree = BST.BST()
	currTree.insertIter(currTree.root, 3)

	visited = []
	currTree.printBST(visited)

if __name__ == "__main__":
	main()