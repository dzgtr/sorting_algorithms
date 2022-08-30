def bubble_sort(pole):
    working_array = pole.copy()
    stop = False
    while not stop:
        stop = True
        for x in range(len(working_array)-1):
            if working_array[x] > working_array[x+1]:
                stop = False
                working_array[x], working_array[x+1] = working_array[x+1], working_array[x]
    return working_array

"""
Bubble sort compares the first two elements, and if the first is greater than the second, it swaps them.
It continues doing this for each pair of adjacent elements to the end of the data set.
It then starts again with the first two elements, repeating until no swaps have occurred on the last pass.
"""