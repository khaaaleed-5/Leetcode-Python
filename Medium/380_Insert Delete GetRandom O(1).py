import random


class Solution:
    def __init__(self):
        self.map = {}
        self.arr = []

    def insert(self, val):
        if val in self.map:
            return False
        self.arr += [val]
        self.map[val] = len(self.arr) - 1
        return True

    def remove(self, val):
        if val not in self.map:
            return False
        ind = self.map[val]
        last_elm = self.arr[-1]
        self.arr[-1] = self.arr[ind]
        self.arr[ind] = last_elm
        self.map[last_elm] = ind
        del self.map[val]
        self.arr.pop()
        return True

    def random_int(self):
        random_index = random.randint(0, len(self.arr) - 1)
        return self.arr[random_index]

    def get(self):
        return self.arr
