
from AVL import AVL
from Node import Node

import testing

def main() -> None:
	nodes = [44, 17, 62, 32, 50, 78, 48, 54, 8]
	tree = AVL()

	for n in nodes:
		tree.insertIter(n)
		
	testing.printInorder(tree.root)

if __name__=="__main__":
	main()