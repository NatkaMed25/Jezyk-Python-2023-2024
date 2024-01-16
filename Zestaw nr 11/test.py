from SingleList import SingleList, Node

def test_remove_tail():
    list = SingleList()
    list.insert_tail(Node(1))
    list.insert_tail(Node(5))
    list.insert_tail(Node(8))
    assert list.remove_tail().data == 8
    assert list.remove_tail().data == 5
    assert list.remove_tail().data == 1
    assert list.count() == 0

def test_join():
    list = SingleList()
    list.insert_tail(Node(1))
    list.insert_tail(Node(2))
    list.insert_tail(Node(3))
    list2 = SingleList()
    list2.insert_tail(Node(4))
    list2.insert_tail(Node(5))
    list2.insert_tail(Node(6))
    list.join(list2)
    assert list2.count() == 0
    for i in range(1, 7):
        assert list.remove_head().data == i

def test_clear():
    lista = SingleList()
    lista.insert_tail(Node(1))
    lista.insert_tail(Node(5))
    lista.insert_tail(Node(8))
    lista.clear()
    assert lista.head is None
    assert lista.tail is None
    assert lista.count() == 0