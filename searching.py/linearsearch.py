# pros :simplicity ,flexiable ,used if the list of elements are unorodered
# cons :not efficient for large list 

def linear_search(list, target):
 
    for i in range(len(list)):
        if list[i] == target:
            return i
         
    return -1


list = [1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 15, 20, 27, 34, 39, 50]
target = 39
result = linear_search(list, target)

if result != -1:
    print (f"The number {target} is located at position: {result}")
else:
    print(f"The number {target} is NOT in the list")
