import hashlib


class Node :
    def __init__(self, key, value, next) :
        self.key = key
        self.value = value
        self.next = next        # 뒤쪽 노드와 연결해주는 속성


class ChainedHash :
    def __init__(self, capacity) :
        self.capacity = capacity
        self.table = [None] * self.capacity

    def hash_value(self, key) :
        if isinstance(key, int) :
            return key % self.capacity      # 키를 배열의 길이로 나눔으로써 해시값을 만들어낸다.

        return int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity       # 문자열 키를 숫자로 변환하는 함수

    def search(self, key) :
        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None :
            if p.key == key :
                return p.value

            p = p.next

        return None

    def add(self, key, value) :
        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None :
            if p.key == key :
                return False

            p = p.next

        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp

        return True

    def remove(self, key) :
        hash = self.hash_value(key)
        p = self.table[hash]
        pp = None

        while p is not None :
            if p.key == key :
                if pp is None :
                    self.table[hash] = p.next
                else :
                    pp.next = p.next

                return True

            pp = pp = p.next

        return False

    def dump(self) :
        for i in range(self.capacity) :
            p = self.table[i]
            print(i, end = '')

            while p is not None :
                print(f'    -> {p.key} ({p.value})', end = '')
                p = p.next

            print()
