def insertion_sort(list):
    for i in range(1, len(list)):
        actual = list[i]
        index = i

        """
        This loop interchanges the two position numbers, as long as the previous number is larger than the current number.
        """

        while index > 0 and list[index - 1] > actual:
            list[index] = list[index - 1]
            index = index - 1
        list[index] = actual

    return list

unordered_list = [39, 45, 32, 4, 2, 85, 43, 7, 18, 16, 5, 67, 32]
ordered_list = insertion_sort(unordered_list)
print(ordered_list)