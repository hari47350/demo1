# Comparing Sequences and Other Types
print((1, 2, 3) < (1, 2, 4))                     # True
print([1, 2, 3] < [1, 2, 4])                     # True
print('ABC' < 'C' < 'Pascal' < 'Python')        # True   unicode(a=65) (c=67) 65<67
print((1, 2, 3, 4) < (1, 2, 4))                  # True
print((1, 2) < (1, 2, -1))                       # True
print((1, 2, 3) == (1.0, 2.0, 3.0))              # True
print((1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4))  # True
