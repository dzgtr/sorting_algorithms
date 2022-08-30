def exchange_sort(pole):
    working_array = pole.copy()
    for item in range(len(working_array)):
        for x in range(item + 1, len(working_array)):
            if working_array[item] > working_array[x]:
                working_array[item], working_array[x] = working_array[x], working_array[item]
    return working_array

"""
Exchange sort works by comparing the first element with all elements above it, swapping where needed,
thereby guaranteeing that the first element is correct for the final sort order.
It then proceeds to do the same for the second element, and so on.
"""