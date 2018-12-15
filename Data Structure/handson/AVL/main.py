from BinarySearch.main import Tree as BS
from BinaryTree.linked import Tree as Order

class Node():
    def __init__(self, key, value, height, left=None, right=None):
        self.key = key
        self.value = value
        self.height = height
        self.left = left
        self.right = right


class Tree(BS, Order):
    def __init__(self, n=None):
        self.root = n

    def put(self, key, value):
        self.root = self.put_item(self.root, key, value)

    def put_item(self, n, key, value):
        if n == None:
            return Node(key, value, 1)
        if n.key > key:
            n.left = self.put_item(n.left, key, value)
        elif n.key < key:
            n.right = self.put_item(n.right, key, value)
        else:
            n.value = value
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        return self.balance(n)

    def balance(self, n):
        if self.bf(n) > 1:
            if self.bf(n.left) < 0:
                n.left = self.rotate_left(n.left)
            n = self.rotate_right(n)
        elif self.bf(n) < -1:
            if self.bf(n.right) > 0:
                n.right = self.rotate_right(n.right)
            n = self.rotate_left(n)
        return n

    def bf(self, n):
        return self.height(n.left) - self.height(n.right)

    def rotate_left(self, n):  # 변경되는 레퍼런스 O(1)
        x = n.right
        n.right = x.left
        x.left = n
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        return x

    def rotate_right(self, n):
        x = n.left
        n.left = x.right
        x.right = n
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        return x

    def height(self, n):
        if n:
            return n.height
        return 0
	
	# def balence_after_delete: TODO

if __name__ == '__main__':
    t = Tree()
    t.put(25, '🍇')
    t.put(37, '🍏')
    t.put(18, '🍌')
    t.put(55, '🍈')
    t.put(22, '🍉')
    t.put(35, '🍊')
    t.put(50, '🍋')
    t.put(63, '🍍')
    t.levelorder(t.root)
    print(t.root.key)
