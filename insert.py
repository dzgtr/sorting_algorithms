def insertion_sort(pole):
    for item in range(len(pole)):
        for current_item in range(item, -1, -1):
            if current_item + 1 < len(pole):
                if pole[current_item+1] < pole[current_item]:
                    pole[current_item+1], pole[current_item] = pole[current_item], pole[current_item+1]

"""
Insert sort works by taking elements from the list one by one and inserting
them in their correct position into a new sorted list. - wikipedia
"""