from collections import namedtuple

# defining the namedtuple( class name, variables )
Point = namedtuple('Point', 'x,y')

pt = Point(1,-5)

print(pt) # Point(x=1, y=-5)

# Accessing the element
print(pt.x, pt.y) #1 -5