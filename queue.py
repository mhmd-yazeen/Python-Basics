# Write a python class queue that implements an basic data structure with the enqueue and dequeue method 
# include the method is_empty to check if the queue is empty

class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, x):
        return self.queue.append(x)
    def dequeue(self):
        return self.queue.pop(0)
    def is_empty(self):
        return len(self.queue) == 0
    def display(self):
        print(self.queue)


d = Queue()
d.enqueue(10)
d.enqueue(20)
d.enqueue(30)
d.dequeue()
d.display()

