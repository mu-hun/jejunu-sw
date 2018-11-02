class Node():
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

class Tree():
	def __init__(self, n=None):
		self.root = n
		self.index = self.root

	def preorder(self, n):
		if n:
			print(str(n.value), ' ', end='')
		else:
			return
		if n.left:
			self.preorder(n.left)
		if n.right:
			self.preorder(n.right)
	
	def inorder(self, n):
		pass
	
	def postorder(self):
		pass
	
	def levelorder(self, root):
		pass
	
	def getHeight(self, root):
		pass
	
	def copy_tree(self, n):
		pass

if __name__ == '__main__':
	t = Tree() # 이진트리 객체 t 생성
	n1 = Node(100) # 8개의 노드 생성
	t.root = n1

	n2 = Node(200)
	n3 = Node(300)
	n4 = Node(400)
	n5 = Node(500)
	n6 = Node(600)
	n7 = Node(700)
	n8 = Node(800)
	
	# TODO: Tree append 구현
	
	t.root.left = n2
	t.root.right = n3

	# n2.left = n4
	# n2.right = n5
	# n3.left = n6
	# n3.right = n7
	# n4.left = n8

	t.root.left.left = n4
	t.root.left.right = n5

	t.root.right.left = n6
	t.root.right.right = n7

	t.root.left.left.left = n8
	
	print('전위순회:\t', end='')
	t.preorder(t.root)
