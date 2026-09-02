class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1

        node = self.cache[key]

        
        if node == self.tail:
            return node.value
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev

        node.prev = self.tail
        node.next = None

        self.tail.next = node
        self.tail = node

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:

            node = self.cache[key]
            node.value = value

           
            if node != self.tail:

                if node.prev:
                    node.prev.next = node.next
                else:
                    self.head = node.next

                if node.next:
                    node.next.prev = node.prev

                node.prev = self.tail
                node.next = None

                self.tail.next = node
                self.tail = node

            return
        if self.length == 0:

            node = Node(key, value)

            self.cache[key] = node

            self.head = node
            self.tail = node

            self.length += 1
        elif self.length < self.capacity:

            node = Node(key, value)

            self.cache[key] = node

            self.tail.next = node
            node.prev = self.tail
            self.tail = node

            self.length += 1

       
        else:
            old_head = self.head

            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None

            del self.cache[old_head.key]

            node = Node(key, value)
            self.cache[key] = node

            if self.tail:
                self.tail.next = node
                node.prev = self.tail
            else:
                self.head = node

            self.tail = node