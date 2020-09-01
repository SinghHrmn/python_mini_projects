from collections import Counter

a = "aaaaaaabbbbbbbbcccc"

my_counter = Counter(a)

print(my_counter)  # Counter({'b': 8, 'a': 7, 'c': 4})

# to get the items in list of tuple form
print(my_counter.items()) # dict_items([('a', 7), ('b', 8), ('c', 4)])

# to print all the keys
print(my_counter.keys()) # dict_keys(['a', 'b', 'c'])

# To print all the values
print(my_counter.values()) # dict_values([7, 8, 4])

# most_common(x) function returns X most common elements in a list of tuples
print(my_counter.most_common(1)[0][0]) # b

# elements provide iterator over the data
print(list(my_counter.elements()))
# ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c']