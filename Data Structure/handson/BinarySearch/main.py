class ListTree:
	def __init__(self, l=[]):
		self.l = l

	def search_by_list(self, left, right, data):
		if left > right:
			return
		mid = right + left // 2
		if self.l[mid] == data:
			return mid
		elif data < self.l[mid]:
			self.search_by_list(left, mid-1, data)
		else:
			self.search_by_list(mid+1, right, data)


class Node():
	def __init__(self, key, value, left=None, right=None):
		self.key = key
		self.value = value
		self.left = left
		self.right = right


class Tree:
	def __init__(self, n):
		self.root = n

	def get(self, k):
		return self.get_item(self.root, k)

	def get_item(self, n, k):
		if n == None:
			return n
		if n.key > k:  # 루트 노드보다 k가 작으먄 왼쪽
			return self.get_item(n.left, k)
		elif n.key < k:  # 루트 노드보다 k가 크면 오른쪽
			return self.get_item(n.right, k)
		else:
			return n.value

	def put(self, k, v):
		self.root = self.put_item(self.root, k, v)

	def put_item(self, n, k, v):
		if n == None:
			return Node(k, v)
		if n.key > k:
			n.left = self.put_item(n.left, k, v)
		elif n.key < k:
			n.right = self.put_item(n.right, k, v)
		else:
			n.value = v  # 끝 노드가 없으면서 left/right 노드가 value 깂이 됨.
		return n

	def min(self):
		if self.root == None:
			return None
		return self.mininum(self.root)

	def mininum(self, n):
		if n.left == None:
			return n
		return self.mininum(n.left)

	def delete_min(self):
		if self.root == None:
			print('Tree is Empty')
		self.root = self.del_min(self.root)

	def del_min(self, n):
		if n.left == None:
			return n.right
		n.left = self.del_min(n.left)
		return n

	def delete(self, k):
		self.root = self.del_node(self.root, k)

	def del_node(self, n, k):
		if n == None:
			return n
		if n.key > k:
			n.left = self.del_node(n.left, k)
		elif n.key < k:
			n.right = self.del_node(n.right, k)
		else:
			if n.right == None:
				return n.left  # 자식이 없으면 None 반환해 삭제,
			if n.left == None:
				return n.right
			target = n
			n = self.mininum(target.right)  # n의 오른쪽 서브 트리의 가장 작은 노드
			n.right = self.del_min(target.right)  # // 위로 올리면서 이전 노드 위치를 삭제
			n.left = target.left
		return n

# TODO: Add test code
