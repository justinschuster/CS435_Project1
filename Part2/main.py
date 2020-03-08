
from AVL import AVL
from Node import Node

import testing

def main() -> None:
	nodes = [44, 17, 78, 32, 50, 88, 48, 62]
	tree = AVL()

	for n in nodes:
		tree.insertIter(n)

	print("\nInorder Traversal:", end=" ")
	testing.printInorder(tree.root)
	print()

	print(str(testing.isValidAVL(tree.root)))

if __name__=="__main__":
	main()