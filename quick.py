import statistics

def quick_sort(pole):
    if len(pole) == 1:
        return pole
    elif len(pole) == 2:
        if pole[0] > pole[1]:
            pole[0], pole[1] = pole[1], pole[0]
        return pole
    else:
        lower_part, higher_part = [], []
        pivot = statistics.median(pole)
        for item in range(len(pole)):
            if pole[item] <= pivot:
                lower_part.append(pole[item])
            else:
                higher_part.append(pole[item])
        pole = quick_sort(lower_part) + quick_sort(higher_part)
        print(pole)
        return pole

"""
Quicksort is a divide-and-conquer algorithm which relies on a partition operation:
To partition an array, an element called a pivot is selected.
All elements smaller than the pivot are moved before it and all greater elements are moved after it.
The lesser and greater sublists are then recursively sorted.
"""