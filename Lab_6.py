from collections import deque

testStack = deque()  #используем Deque для представления стека в виде двусвязного списка

testStack.append('first')
print(testStack)
testStack.append('second')
print(testStack)
testStack.append('third')
print(testStack)

testStack.pop()
print(testStack)
testStack.pop()
print(testStack)

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:

    def __init__(self):
        self.head = Node("head")
        self.size = 0

    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-2]

    def isEmpty(self):
        return self.size == 0

    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("Стек пуст")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value


mnlStack = Stack()
mnlStack.push('first')
print(mnlStack)
mnlStack.push('second')
print(mnlStack)
mnlStack.push('third')
print(mnlStack)

mnlStack.pop()
print(mnlStack)
mnlStack.pop()
print(mnlStack)