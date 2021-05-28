# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 09:49:12 2021

@author: lee
"""

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.len = 0


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.queue.append(x)
        self.len += 1


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        len_q = len(self.queue)
        if len_q == 0:
            temp = None
        elif len_q == 1:
            temp = self.queue[0]
            self.queue = []
            self.len -= 1
        else:
            temp = self.queue[0]
            self.queue = self.queue[1::]
            self.len -= 1
        return temp

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.queue:
            return None
        else:
            return self.queue[0]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.len > 0:
            return False
        else:
            return True



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()