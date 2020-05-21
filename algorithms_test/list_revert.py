class Node:
    def __init__(self, next, value):
        self.next = next
        self.value = value


#输入是一个NodeList链表
def reverse(nodeList):
    if nodeList is None or nodeList.next is None:
        return nodeList
    head = None
    next = nodeList
    tmp = None
    while next is not None:
        tmp = next
        next = next.next
        tmp.next = head
        head = tmp
    return head


if __name__ == '__main__':
    n3 = Node(None,3)
    n2 = Node(n3, 2)
    n1 = Node(n2, 1)

    res = reverse(n3)
    while res is not None:
        print(res.value)
        res = res.next





