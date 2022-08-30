import random
import bubble
import exchange
import insert
import selection
import comb
import bucket
import merge
import quick

def random_list(number):
    while True:
        rand = random.randint(0, number - 1)
        if rand not in pole:
            pole.append(rand)
        if len(pole) == number:
            break


if __name__ == '__main__':
    pole = []
    random_list(21)
    print(pole)
#    pole = bubble.bubble_sort(pole)
#    pole = exchange.exchange_sort(pole)
#    pole = insert.insertion_sort(pole)
#    pole = selection.selection_sort(pole)
#    pole = comb.comb_sort(pole)
    pole = quick.quick_sort(pole)
###############    bucket.bucket_sort(pole)
###############    pole = merge.merge_sort(pole)

    print(pole)