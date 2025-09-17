# The .format() method in Python is used to insert variables into a string dynamically.
# It helps us avoid messy string concatenation like this:
name = "Hari"
age = 21
print("My name is " + name + ", I am " + str(age) + " years old.")

# using format
print("My name is {}, I am {} years old.".format(name, age))

# example 2
print('{0}, {1}, {2}'.format('a', 'b', 'c'))

print('{}, {}, {}'.format('a', 'b', 'c') ) 

print('{2}, {1}, {0}'.format('a', 'b', 'c'))

print('{2}, {1}, {0}'.format(*'abc')    )  # unpacking argument sequence

'{0}{1}{0}'.format('abra', 'cad')   # arguments' indices can be repeated