import math
from itertools import islice
# Use generator

class PrimeNumbers:
    def __init__(self,start, end):
        self.start = start
        self.end = end

    def isPrimeNumber(self, k):
        if k < 2:
            return False

        for i in range(2, int(math.sqrt(k))):
            if k % i == 0:
                return False
        return True
    def __iter__(self):
        for k in range(self.start, self.end+1):
            if self.isPrimeNumber(k):
                yield k

for x in PrimeNumbers(1,100):
    print(x)


class floatRange:
    def __init__(self,start,end,step=0.1):
        self.start = start
        self.end = end
        self.step = step
    def __iter__(self):
        t = self.start
        while t <= self.end:
            yield t
            t += self.step
    def __reversed__(self):
        t = self.end
        while t >= self.start:
            yield t
            t -= self.step

# Use built-in functions

f = open("TextSplitExample.txt")
for x in islice(f, 1, 5):
    print(x)



