def exchange_sort(pole):
    for item in range(len(pole)):
        for x in range(item + 1, len(pole)):
            if pole[item] > pole[x]:
                pole[item], pole[x] = pole[x], pole[item]

"""
Exchange sort works by comparing the first element with all elements above it, swapping where needed,
thereby guaranteeing that the first element is correct for the final sort order.
It then proceeds to do the same for the second element, and so on
"""