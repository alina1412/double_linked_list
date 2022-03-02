from ..node import Node


def create_node_list(lst):
    head = Node(0)
    cur = head
    for e in lst:
        newn = Node(e)
        cur.next = newn
        newn.prev = cur
        cur = cur.next
    if head.next:
        head.next.prev = None
    return head.next


def test__create():
    node = Node(12)
    assert node.val == 12

    d = {1: 2, 3: 4}
    node = Node(d)
    assert node.val == d


def test__move_left_right():
    arr = list(range(30))
    n = len(arr)
    head = create_node_list(arr)
    for i in range(n):
        node = head.move_right(i)
        assert node.val == arr[i]
        for j in range(n - i):
            assert node.move_right(j).move_left(j) == node


def test__put_before():
    arr0 = [1, 3, 5]
    arr1 = [0, 1, 2, 3, 4, 5]
    head = create_node_list(arr0)
    head.move_right(0).put_before(0)
    head = head.prev
    head.move_right(3).put_before(4)
    head.move_right(2).put_before(2)
    cur = head
    for v in arr1:
        assert v == cur.val
        cur = cur.next
