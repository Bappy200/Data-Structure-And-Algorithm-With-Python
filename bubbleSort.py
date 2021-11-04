def bubble_sort(items):
    n = len(items)
    for i in range(n-1):
        for j in range(n-i-1):
            if(items[j] > items[j+1]):
                items[j], items[j+1] = items[j+1], items[j]
    
    return items

numbers = [3, 67, 2, 30, 59, 99, 40, 1, 2]
sortNumber = bubble_sort(numbers)
print(sortNumber)
