from .node import Node


class BidirectionalLinkedList:

    def __init__(self, collection=None):
        self.size = 0
        self.beg = Node("beg")
        self.end = Node('end')
        self.beg.next = self.end
        self.end.prev = self.beg

        if collection:
            for element in collection:
                self.addAtTail(element)

        self.append = self.addAtTail
        self.appendleft = self.addAtHead

    def popleft(self):
        ret = self.get(0)
        self.deleteAtIndex(0)
        return ret

    def pop(self):
        ret = self.get(self.size - 1)
        self.deleteAtIndex(self.size - 1)
        return ret

    def __len__(self):
        return self.size

    def __str__(self):
        s = []
        p = self.beg.next
        while p != self.end:
            s.append(str(p.val))
            p = p.next
        return "MyLinkedList([" + ", ".join(s) + "])"

    def __getitem__(self, key):
        return self.get(key)

    # 0    1    2
    # n -> n -> n -> None
    #

    def get(self, index: int) -> int:
        if not 0 <= index < self.size:
            return -1
        return self.beg.next.move_right(index).val

    def addAtHead(self, val: int) -> None:
        self.beg.next.put_before(val)
        self.size += 1

    # beg - * - * - end
    #  -1    0   1   2
    # addAtIndex(2)

    def addAtTail(self, val: int) -> None:
        self.end.put_before(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return

        elif index <= self.size // 2:
            # move right
            cur = self.beg.next.move_right(index)
            cur.put_before(val)
        else:
            # move-left
            steps = self.size - index
            cur = self.end.move_left(steps)
            cur.put_before(val)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size or index < 0:
            return

        if index <= self.size // 2:
            cur = self.beg.next.move_right(index)
            leftnode = cur.prev
            leftnode.next = cur.next
            cur.next.prev = leftnode
        else:
            steps = self.size - index
            cur = self.end.move_left(steps)
            leftnode = cur.prev
            leftnode.next = cur.next
            cur.next.prev = leftnode

        self.size -= 1
