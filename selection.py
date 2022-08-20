def selection_sort(pole):
    for item in range(len(pole)):
        indexswap = pole.index(min(pole[item:]))
        pole[item], pole[indexswap] = pole[indexswap], pole[item]

"""
Selection sort finds the minimum value, swaps it with the value in the first position
and repeats these steps for the remainder of the list.
"""