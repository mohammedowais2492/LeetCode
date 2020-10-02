# Problem number 933
from collections import deque

class RecentCounter:

    def __init__(self):
        self.requests = deque()
        self.number = 0

    def ping(self, t: int) -> int:
        self.requests.append(t)
        self.number += 1
        while t - self.requests[0] > 3000:
            self.requests.popleft()
            self.number -= 1
        return self.number

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
