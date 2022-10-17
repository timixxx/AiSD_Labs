class Node:
    def __init__ (self,value = None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def contains(self, value):
        last = self.head
        while (last):
            if value == last.value:
                return True
            else:
                last = last.next
        return False

    def addToEnd(self, value):
        newnode = Node(value)
        if self.head is None:
            self.head = newnode
            return
        last = self.head
        while (last.next):
            last = last.next
        last.next = newnode

    def get(self, index):
        last = self.head
        nodeIndex = 0
        while nodeIndex <= index:
            if nodeIndex == index:
                return last.value
            nodeIndex = nodeIndex + 1
            last = last.next

    def removeNode(self, rmvalue):
        headvalue = self.head

        if headvalue is not None:
            if headvalue.value == rmvalue:
                self.head = headvalue.next
                headvalue = None
                return
        while headvalue is not None:
            if headvalue.value == rmvalue:
                break
            lastvalue = headvalue
            headvalue = headvalue.next
        if headvalue == None:
            return
        lastvalue.next = headvalue.next
        headvalue = None
        print("Элемент", rmvalue,"удалён")



list1 = LinkedList()

list1.addToEnd(10)
list1.addToEnd(2)
list1.addToEnd(5)
print("Содержит ли список элемент 10:", list1.contains(10))
print("Содержит ли список элемент 2:", list1.contains(2))
print("Содержит ли список элемент 3:", list1.contains(3))
print("Элемент с индексом 1:", list1.get(1))
list1.removeNode(2)
print("Содержит ли список элемент 2:", list1.contains(2))

print("Элемент с индексом 0:", list1.get(0))
print("Элемент с индексом 1:", list1.get(1))