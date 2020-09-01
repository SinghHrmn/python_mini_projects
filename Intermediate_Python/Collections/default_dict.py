from collections import defaultdict


# initialize defaultdict with default type
d1 = defaultdict(int)
d1['a'] = 1
d1['b'] = 2
print(d1['c']) # 0

def my_value():
    return 45

# initialize defaultdict with default callable
d2 = defaultdict(my_value)

d2['a'] = 1
d2['b'] = 2
print(d2['c']) # 45


