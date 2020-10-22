class Node :
    def __init__(self, key, value, left, right) :
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree :
    def __init__(self) :
        self.root = None

    def search(self, key) :
        p = self.root

        while True :
            if p is None :
                return None

            if key == p.key :
                return p.value
            elif key < p.key :
                p = p.left
            else :
                p = p.right

    def add(self, key, value) :
        def add_node(node, key, value) :
            if key == node.key :
                return False
            elif key < node.key :
                if node.left is None :
                    node.left = Node(key, value, None, None)
                else :
                    add_node(node.left, key, value)
            else :
                if node.right is None :
                    node.right = Node(key, value, None, None)
                else :
                    add_node(node.right, key, value)

            return True

        if self.root is None :
            self.root = Node(key, value, None, None)        # 루트 노드가 없는 경우(트리가 비어있는 경우)
        else :
            return add_node(self.root, key, value)          # 트리가 비어있지 않은 경우

    def remove(self, key) :
        p = self.rot
        parent = None
        is_left_child = True

        # 삭제할 키를 검색하는 while
        while True :
            if p is None :
                return False

            if key == p.key :
                break
            else :
                parent = p

                if key < p.key :
                    is_left_child = True
                    p = p.left
                else :
                    is_left_child = False
                    p = p.right

        if p.left is None :
            if p is self.root :
                self.root = p.right
            elif is_left_child :
                parent.left = p.right
            else :
                parent.right = p.right

        # 진행중

