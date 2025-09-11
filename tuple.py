# An ordered collection of items that cannot be changed (immutable).
# allows duplicates
t = 123, 10, 'hello!'
print(t[0])

print(t)
(12345, 54321, 'hello!')
# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print(u)
# output ->((123, 10, 'hello!'), (1, 2, 3, 4, 5))
# Tuples are immutable:
# t[0] = 88888

#  but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
print(v)

# 0 and singleton tuple 
empty = ()
singleton = 'hello',    # <-- note trailing comma
print(len(empty))
print(len(singleton))
