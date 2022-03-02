class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

    def __repr__(self) -> str:
        return f"Node(val = {self.val})"

    def move_right(self, steps):
        cur = self
        for _ in range(steps):
            cur = cur.next
        return cur

    def move_left(self, steps):
        cur = self
        for _ in range(steps):
            cur = cur.prev
        return cur

    def put_before(self, val):
        newn = Node(val)
        leftnode = self.prev
        newn.next = self
        self.prev = newn
        newn.prev = leftnode
        if leftnode:
            leftnode.next = newn
