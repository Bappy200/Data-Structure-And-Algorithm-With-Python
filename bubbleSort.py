def bubble_sort(items):
    n = len(items)
    for i in range(n-1):
        is_change = True
        for j in range(n-i-1):
            if(items[j] > items[j+1]):
                items[j], items[j+1] = items[j+1], items[j]
                is_change = False
        if is_change:
            return items 
    
    return items

numbers = [3, 67, 30, 2, 59, 99]
sortNumber = bubble_sort(numbers)
print(sortNumber)
