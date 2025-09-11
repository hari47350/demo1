# Data stuctures
# list -append,insert,extend,remove,pop,clear,index,count,sort,reverse,copy
# list properties ->mutable,ordered
fruits = ['orange', 'apple', 'papaya', 'banana', 'grapes', 'apple', 'banana']

print(fruits.count('apple'))
print(fruits.count('pineapple'))

print(fruits.index('banana'))
print(fruits.index('banana', 4))

fruits.remove('grapes')
print(fruits)

fruits.reverse()
print(fruits)

fruits.append('mango')
print(fruits)

fruits.sort()
print(fruits)

fruits.pop()
print(fruits)

fruits.clear()
print(fruits)

# stacks -> using LIFO last in first out 
# OPERATIONS : Append,pop

stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)  

stack.pop()
print(stack)  # Output: [3, 4, 5, 6]

stack.pop()
stack.pop()
print(stack) 

# Using Lists as Queues
# queue -> FIFO 

from collections import deque
queue = deque(["ram", "siddu", "sree"])
queue.append("teju")           # Teju arrives
queue.append("Goutham")          # Goutham arrives
queue.popleft()                 # The first to arrive now leaves

queue.popleft()                 # The second to arrive now leaves

queue                           # Remaining queue in order of arrival


             


