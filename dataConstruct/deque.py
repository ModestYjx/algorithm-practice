from collections import deque

d = deque([1, 2, 3, 4, 5])
print(d)
d.extendleft([0])
d.extend([6, 7, 8])
print(d)
print(len(d))