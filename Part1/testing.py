from Node import Node 

# helper function to print out preorder traversal for testing
def printPreorder(root: Node, visited=[]) -> None:
	if root is None or root.data is None:
		return

	print(root.data, end=" ")
	visited.append(root.data)

	if (root.left is not None and root.right not in visited):
		printPreorder(root.left, visited)
	if (root.right is not None and root.right not in visited):	
		printPreorder(root.right, visited)

	return visited


# test insert methods
class TestMethods:

	def testInsert(root):
		answerPreorder = [5, 4, 1, 7, 9]
		count = 0

		result = printPreorder(root)	
		while (count < len(answerPreorder) - 1):
			if (answerPreorder[count] != result[count]):
				print("Did not insert correctly. i: %d, j: %d"% (answerPreorder[count], result[count]))
				break 
			count = count + 1

		print("\ninserted correctly")