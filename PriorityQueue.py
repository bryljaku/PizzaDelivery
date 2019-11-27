import collections
import heapq

class HeapPriorityQueue:
    def __init__(self):
        self.vals = []

    def empty(self):
        return len(self.vals) == 0

    def put(self, item, priority):
        heapq.heappush(self.vals, (priority, item))

    def get(self):
        return heapq.heappop(self.vals)[1]
