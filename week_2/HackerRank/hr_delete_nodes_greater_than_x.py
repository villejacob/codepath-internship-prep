'''
Remove nodes with value greater than x
'''


def removeNodes(list, x):
    current = LinkedListNode(0)
    head = current
    current.next = list
    traveller = list

    while traveller:
        if traveller.val <= x:
            current.next = traveller
            current = traveller
        traveller = traveller.next
    current.next = None

    return head.next