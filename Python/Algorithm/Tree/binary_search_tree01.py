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
                    add_node(node.left, key, value)             # 자신의 키에 맞는 자리까지 비교하면서 내려간다.
            else :
                if node.right is None :
                    node.right = Node(key, value, None, None)
                else :
                    add_node(node.right, key, value)            # 자신의 키에 맞는 자리까지 비교하면서 내려간다.

            return True

        if self.root is None :
            self.root = Node(key, value, None, None)        # 루트 노드가 없는 경우(트리가 비어있는 경우)
        else :
            return add_node(self.root, key, value)          # 트리가 비어있지 않은 경우

    def remove(self, key) :
        p = self.root
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

        if p.left is None :                     # 삭제할 노드의 왼쪽 자식노드가 없을 경우
            if p is self.root :                     # 삭제할 노드가 루트노드라면
                self.root = p.right                 # 루트 노드를 오른쪽 자식 노드로 덮어씌운다.(저장)
            elif is_left_child :                    # 삭제할 노드가 부모 노드 기준으로 왼쪽 자식 노드라면
                parent.left = p.right               # 부모의 왼쪽 자식 노드를 가리키는 속성을 왼쪽 자식노드의 오른쪽 자식 노드로 바꿔버린다.
            else :                                  # 삭제할 노드가 부모 노드 기준으로 오른쪽 자식 노드라면
                parent.right = p.right              # 부모의 오른쪽 자식 노드를 가리키는 속성을 오른쪽 자식 노드의 자식 노드로 바꿔버린다.
        elif p.right is None :                  # 삭제할 노드의 오른쪽 자식노드가 없을 경우
            if p is self.root :                     # 삭제할 노드가 루트 노드라면
                self.root = p.left                  # 루트 노드를 왼쪽 자식 노드로 덮어씌운다.
            elif is_left_child :                    # 삭제할 노드가 부모 노드 기준으로 왼쪽 자식 노드라면
                parent.left = p.left                # 부모의 왼쪽 자식 노드를 가리키는 속성을 왼쪽 자식 노드의 자식 노드로 바꿔버린다.
            else :                                  # 삭제할 노드가 부모 노드 기준으로 오른쪽 자식 노드라면
                parent.right = p.right              # 부모의 오른쪽 자식 노드를 가리키는 속성을 오른쪽 자식 노드의 오른쪽 자식 노드로 바꿔버린다.
        else :                                  # 왼쪽 오른쪽 자식노드가 있는 경우
            parent = p                              #
            left = p.left
            is_left_child = True

            while left.right is not None :
                parent = left
                left = left.right
                is_left_child = False

            p.key = left.key
            p.value = left.value

            if is_left_child :
                parent.left = left.left
            else :
                parent.right = left.left

        return True