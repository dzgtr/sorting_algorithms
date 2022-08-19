import random
import bubble
import exchange
import insert


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
#    bubble.bubble_sort(pole)
#    exchange.exchange_sort(pole)
#    insert.insertion_sort(pole)
    print(pole)