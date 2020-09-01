from collections import deque

d = deque()

d.append(1)
d.append(2)

d.appendleft(3)


d.pop()
d.popleft()

d.extend([4,5,6])
d.extendleft([9,8,7])

print(d)

# rotate the array one position
d.rotate(1)

print(d)

# rotate the array one position alternatively
d.rotate(-1)

print(d)


d.clear()
