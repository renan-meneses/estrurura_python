
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

class Queue:
    
    def __init__(self):
        self.__queue = []
        
    def enqueue(self, value):
        self.__queue.append(value)
        
    def dequeue(self):
        return self.__queue.pop(0)
        
    def show(self):
        print("Queue: {}".format(self.__queue))

def main():
    queue = Queue()

    for _ in xrange(0, 10):
        queue.enqueue(random.randint(10,99))

    queue.show()

    queue.dequeue()
    queue.dequeue()

    queue.show()

if __name__ == "__main__":
    main()
