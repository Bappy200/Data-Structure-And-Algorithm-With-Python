def selection_sort(items):
    length = len(items)
    for i in range(length):
        min_index = i
        for j in range(min_index + 1, length):
            if items[min_index] > items[j]:
                min_index = j

        if min_index != i:
            items[i], items[min_index] = items[min_index], items[i]


data = [-2, 45, 0, 11, -9]
selection_sort(data)
print(data)

