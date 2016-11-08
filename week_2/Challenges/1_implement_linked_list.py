class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    def getNext(self):
        if self.next:
            return self.next.value
        else:
            return None

    def setNext(self, value):
        if self.next:
            self.next.value = value


class LinkedList:
    def __init__(self):
        self.head = None

    def setValuesFromArray(self, array):
        if not array:
            return None
        self.head = ListNode(array[0])
        current = self.head
        # For all remaining values in the array
        for value in array[1:]:
            current.next = ListNode(value)
            current = current.next


my_list = LinkedList()
my_list.head = ListNode(0)
input_array = [1, 2, 3, 4, 5]

my_list.setValuesFromArray(input_array)
ptr = my_list.head

output = []

while ptr:
    output.append(str(ptr.value))
    ptr = ptr.next

print " -> ".join(output)
