def binary_search(numbers, search_number):
    left = 0
    right = len(numbers) - 1


    while(left < right):
        mid = (left + right) // 2
        if numbers[mid] == search_number:
            return numbers[mid]
        elif numbers[mid] > search_number:
            right = mid - 1
        else:
            left = mid + 1

    return -1


result = binary_search([1, 3, 4, 5, 12, 16, 25, 29, 30, 45, 55, 67], 56)
print(result)
