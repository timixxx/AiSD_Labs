class Queue:

    def __init__(self, max_size, size=0, front=0, rear=0):
        self.queue = [[] for i in range(max_size)]
        self.max_size = max_size
        self.size = size
        self.front = front
        self.rear = rear

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.max_size

    def enqueue(self, value):
        if not self.isFull():
            self.queue[self.rear] = value
            self.rear = int((self.rear + 1) % self.max_size)
            self.size += 1
        else:
            print('Очередь заполнена')

    def dequeue(self):
        if not self.isEmpty():
            print(self.queue[self.front], 'удалён')
            self.front = int((self.front + 1) % self.max_size)
            self.size -= 1
        else:
            print('Очередь пуста')

    def show(self):
        print('Очередь:')
        for i in range(self.size):
            print(self.queue[int((i + self.front) % self.max_size)],)

testQueue = Queue(2)
testQueue.enqueue('first')
testQueue.show()
testQueue.enqueue('second')
testQueue.show()
testQueue.enqueue('third')
testQueue.show()

testQueue.dequeue()
testQueue.show()
testQueue.dequeue()
testQueue.show()