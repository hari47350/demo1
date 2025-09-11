squares = []
for x in range(10):
    squares.append(x**2)

print(squares)

# optimized
squares = list(map(lambda x: x**2, range(10)))
# or
squares = [x**2 for x in range(10)]

# example for and if
print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])

# contains complex expression and nested loops 
from math import pi
print([str(round(pi, i)) for i in range(1, 6)])
# output -> ['3.1', '3.14', '3.142', '3.1416', '3.14159']

# Use Parentheses for Tuples

# To create a list of tuples, wrap the tuple in parentheses:

print([(x, x**2) for x in range(6)])