
from AVL import AVL
from Node import Node

import testing

def main() -> None:
	tree = AVL()

	tree.insertIter(5)
	testing.printInorder(tree.root)

if __name__=="__main__":
	main()