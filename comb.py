def comb_sort(pole):
    working_array = pole.copy()
    k = int(len(pole) / 1.3)
    for twice in range(2):
        while k > 0:
            for item in range(len(working_array)):
                if item+k < len(working_array):
                    if working_array[item] > working_array[item+k]:
                        working_array[item], working_array[item+k] = working_array[item+k], working_array[item]
            k = int(k/1.3)
            print(k)
        k += 1
    return working_array

"""
Comb sort is based on Bubble sort with idea to eliminate turtles, or small values near the end of the list
since in a bubble sort these slow the sorting down tremendously. 
Rabbits, large values around the beginning of the list, do not pose a problem in bubble sort.
In bubble sort, when any two elements are compared, they always have a gap (distance from each other) of 1.
The basic idea of comb sort is that the gap can be much more than 1. 
The inner loop of bubble sort, which does the actual swap, is modified such that the gap between
swapped elements goes down (for each iteration of outer loop) in steps of a "shrink factor" k: [ n/k, n/k2, n/k3, ..., 1 
"""