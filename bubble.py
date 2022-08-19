def bubble_sort(pole):
    while True:
        stop = True
        for x in range(len(pole)):
            if x+1 < len(pole):
                if pole[x] > pole[x+1]:
                    stop = False
                    pole[x], pole[x+1] = pole[x+1], pole[x]
        if stop:
            break

"""
Bubble sort compares the first two elements, and if the first is greater than the second, it swaps them.
It continues doing this for each pair of adjacent elements to the end of the data set.
It then starts again with the first two elements, repeating until no swaps have occurred on the last pass.
"""