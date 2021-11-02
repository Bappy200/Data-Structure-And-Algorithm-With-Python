def liner_search(lists, searchitem):
    for item in lists:
        if item == searchitem:
            return True
    
    return False


lists = [34, 56, 7, 67, 56, 51]
result = liner_search(lists, 47)
print(result)
