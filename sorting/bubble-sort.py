def bubble_sort(list):
    length = len(list)
    for i in range(length):
        for j in range(0, (length-i) - 1):


            if list[j] > list[j + 1]:
                auxiliar = list[j + 1]
                list[j + 1] = list[j]
                list[j] = auxiliar
    return list

unordered_list = [3, 6, 7, 8, 3, 45, 23, 0, 16, 26, 6, 7, 50]
ordered_list = bubble_sort(unordered_list)
print(ordered_list)

# In the programming world, sorting and searching algorithms are fundamental for data manipulation
# optimization of task