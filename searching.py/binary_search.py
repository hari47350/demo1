# used in searching alogorithm if list of elements are sorted 
#  fewer comparisions due to divide th elidt into two halfs
# Higher deployment complexity: Compared to linear search, binary search is more complex to implement due to its recursive nature.
def binary_search(list, target, start, end ):
    if start > end:
        return -1

    mid = (start + end) // 2
    if list[mid] == target:
        return mid
    elif list[mid] < target:
        return binary_search(list, target, mid+ 1, end)
    else:
        return binary_search(list, target, start, mid - 1)
       
# Example of use
list = [1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 15, 20, 27, 34, 39, 50]
target = 27
start_search = 0
end_search = len(list) - 1

result = binary_search(list, target, start_search, end_search)

if result != -1:
    print(f"The number {target} is in position: {result}.")
else:
    print(f"The number {target} is NOT in the list")