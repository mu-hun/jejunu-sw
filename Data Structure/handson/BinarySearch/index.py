class ListTree:
    def __init__(self, l=[]):
        self.l = l

    def search_by_list(self, left, right, data):
        if left > right:
            return
        mid = right + left // 2
        if self.l[mid] == data:
            return mid
        if data < self.l[mid]:
            self.search_by_list(left, mid-1, data)
        else:
            self.search_by_list(mid+1, right, data)


class Node():
    def __init__(self, key, value, left=None, right=None):
        self.key: int = key
        self.value: str = value
        self.left: Node = left
        self.right: Node = right


class Tree:
    def __init__(self, n=None):
        self.root = n

    def get(self, k):
        return self.get_item(self.root, k)

    def get_item(self, n, k):
        if n == None:
            return n
        if n.key > k:  # 루트 노드보다 k가 작으면 왼쪽
            return self.get_item(n.left, k)
        if n.key < k:  # 루트 노드보다 k가 크면 오른쪽
            return self.get_item(n.right, k)
        return n.value

    def put(self, k, v):
        self.root = self.put_item(self.root, k, v)

    def put_item(self, n, k, v):
        if n == None:
            return Node(k, v)
        if n.key > k:
            n.left = self.put_item(n.left, k, v)
        if n.key < k:
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
        if n == None:  # case 1
            return n

        if n.key > k:
            n.left = self.del_node(n.left, k)
            return n
        if n.key < k:
            n.right = self.del_node(n.right, k)
            return n

        # 삭제할 노드 찾았음 - 그 왼쪽 자식으로 대치 (case 2)
        if n.right == None:
            return n.left
        if n.left == None:
            return n.right

        # case 3
        target = n
        n = self.mininum(target.right)  # n의 오른쪽 서브 트리의 가장 작은 노드
        n.right = self.del_min(target.right)  # // 위로 올리면서 이전 노드 위치를 삭제
        n.left = target.left
        return n

    def getHeight(self):
        c, i = self.root, 0
        while c:
            if c.left:
                c = c.left
            else:
                c = c.right
            i = i + 1
        return i


if __name__ == '__main__':
    t = Tree()
    t.put(10, '10')
    t.put(20, '20')
    t.put(30, '30')
    t.put(40, '40')
    t.put(50, '50')
    t.put(60, '60')
    t.put(70, '70')
    print(t.min().key)
    t.delete_min()
    print(t.min().key)
    t.delete(40)
    print(t.getHeight())
