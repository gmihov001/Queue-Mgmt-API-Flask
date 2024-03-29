from random import randint

class Queue:
    def __init__(self):
        self.current_queue = []

    def enqueue(self, item):
        self.current_queue.insert(0, item)
        return self.current_queue

    def dequeue(self):
        return self.current_queue.pop()        

    def get_queue(self):
        return self.current_queue

    def get_size(self):
        return len(self.current_queue)       
