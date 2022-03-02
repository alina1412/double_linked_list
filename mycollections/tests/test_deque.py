from ..deque import BidirectionalLinkedList


def test__of_init():
    # __init__, __len__
    lst = BidirectionalLinkedList()
    assert len(lst) == 0


def test__addAtHead():
    lst = BidirectionalLinkedList()
    assert lst.get(12) == -1
    assert lst.get(-1) == -1
    assert lst.get(0) == -1

    lst.addAtHead(1)
    lst.addAtHead(2)
    lst.addAtHead(3)
    assert len(lst) == 3
    assert lst.get(0) == 3
    assert lst.get(1) == 2
    assert lst.get(2) == 1
    assert lst.get(3) == -1


def test__addAtTail_and_get():
    lst = BidirectionalLinkedList()
    lst.addAtHead(1)
    lst.addAtHead(2)
    lst.addAtHead(3)
    lst.addAtTail(0)
    assert len(lst) == 4
    assert lst.get(3) == 0

    lst = BidirectionalLinkedList()
    lst.addAtTail(0)
    assert len(lst) == 1
    assert lst.get(0) == 0


def test__addAtIndex():
    # ### addAtIndex
    lst = BidirectionalLinkedList()
    lst.addAtIndex(0, 0)
    assert len(lst) == 1
    assert lst.get(0) == 0

    lst.addAtIndex(1, 5)
    assert len(lst) == 2
    assert lst.get(1) == 5


def test__deleteAtIndex():
    # deleteAtIndex
    lst = BidirectionalLinkedList()
    lst.addAtHead(1)
    lst.addAtHead(2)        # 2 1
    lst.deleteAtIndex(1)    # 2
    assert len(lst) == 1
    assert lst.get(0) == 2  # 2
    lst.addAtTail(7)        # 2 7
    lst.addAtTail(8)        # 2 7 8
    assert lst.get(0) == 2
    assert lst.get(1) == 7  # 2 7 8
    assert lst.get(2) == 8  # 2 7 8
    assert len(lst) == 3
    lst.deleteAtIndex(2)    # 2 7 8 -> 2 7
    assert len(lst) == 2
    assert lst.get(0) == 2  # 2 7
    assert lst.get(1) == 7  # 2 7
    lst.deleteAtIndex(10)
    lst.deleteAtIndex(-10)
    lst.addAtHead(0)        # 0 2 7
    assert lst.get(0) == 0
    assert lst.get(1) == 2
    lst.deleteAtIndex(1)    # 0 7
    assert lst.get(0) == 0
    assert lst.get(1) == 7
    lst.addAtTail(8)        # 0 7 8
    lst.deleteAtIndex(1)    # 0 8
    lst.deleteAtIndex(1)    # 0
    lst.deleteAtIndex(1)    # 0
    assert lst.get(0) == 0


def test__getitem__():
    lst = BidirectionalLinkedList()
    lst.addAtHead(1)


def test__create_node_list():
    lst = BidirectionalLinkedList()
    arr = [1, 2, 3, 4]
    for elem in arr:
        lst.addAtTail(elem)
    assert len(lst) == 4
    for i in range(len(arr)):
        assert lst.get(i) == arr[i]
    # print(lst)
