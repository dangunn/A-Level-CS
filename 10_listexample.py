class Stack:

    def __init__(self, size):
        self.data = [0] * size
        self.size = size
        self.top = -1

    def push(self, value):
        if (self.top == (self.size - 1)):
            print("Error this stack is full, cannot push", value)
            return
        else:
            self.top += 1
            self.data[self.top] = value

    def pop(self):
        if self.top < 0:
            print("Error, the stack is empty")
            return None
        else:
            self.top -= 1
            return self.data[self.top+1]

class Queue:
    def __init__(self, size):
        self.data = [0] * size
        self.front = -1
        self.back = -1
        self.size = size

    def enqueue(self, value):
        if ((self.back + 1) % self.size == self.front):
            print("Error the queue is full")
        else:
            if self.front == -1:
                self.front = 0

            self.back += 1
            self.back %= self.size
            self.data[self.back] = value

    def dequeue(self):
        if self.front == -1:
            print("Error the queue is empty")
            return None
        else:
            val = self.data[self.front]
            if self.front == self.back:  # Only one thing left
                self.front = -1
                self.back = -1
            else:
                self.front += 1
                self.front %= self.size
            return val


class List:
    def __init__(self):


    def append(self):

    def delete(self):

    def insert(self):