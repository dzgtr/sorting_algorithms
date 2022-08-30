def selection_sort(pole):
    working_array = pole.copy()
    for item in range(len(working_array)):
        indexswap = working_array.index(min(working_array[item:]))
        working_array[item], working_array[indexswap] = working_array[indexswap], working_array[item]
    return working_array

"""
Selection sort finds the minimum value, swaps it with the value in the first position
and repeats these steps for the remainder of the list.
"""