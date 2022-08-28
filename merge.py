def merge_sort(pole):
    part_one, part_two = [], []
    if len(pole) % 2 == 0:
        lenhalf = int(len(pole)/2)
        if len(pole) > 2:
            part_one = pole[:lenhalf:]
            part_two = pole[lenhalf::]
            merge_sort(part_one)
            merge_sort(part_two)
            merging(part_one, part_two)
            return pole
        else:
            if pole[0] > pole[1]:
                pole[0], pole[1] = pole[1], pole[0]
            return pole
    else:
        lenhalf = int(len(pole)/2)
        if len(pole) > 2:
            part_one = pole[:lenhalf + 1:]
            part_two = pole[lenhalf + 1::]
            merge_sort(part_one)
            merge_sort(part_two)

        else:
            print(pole)
            return pole

def merging(part_one, part_two):
    merged = part_one
    print(merged)
    for x in range(len(merged)):
        for y in range(len(part_two)):
            if merged[x] > part_two[y]:
                merged[x].insert(part_two[y])
    print(merged)
"""
Merge sort starts by comparing every two elements (i.e., 1 with 2, then 3 with 4...) and swapping them
if the first should come after the second. It then merges each of the resulting lists of two into lists of four,
then merges those lists of four, and so on; until at last two lists are merged into the final sorted list.
"""