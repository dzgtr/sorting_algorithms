def insertion_sort(pole):
    working_array = pole.copy()
    for item in range(len(working_array)-1):
        for current_item in range(item, -1, -1):
            if working_array[current_item+1] < working_array[current_item]:
                working_array[current_item+1], working_array[current_item] = working_array[current_item], working_array[current_item+1]
    return working_array

"""
Insert sort works by taking elements from the list one by one and inserting
them in their correct position into a new sorted list.
"""