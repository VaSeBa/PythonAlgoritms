import random


def binary_search(list, item):
    low = 0
    high = len(list) - 1
    step = 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        print(f"step = {step}")
        step += 1
        if guess == item:  # число найдено
            return mid
        if guess > item:  # число больше
            high = mid - 1
        else:  # число меньше
            low = mid + 1
    return None


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers2 = [x for x in range(1, 10001)]
target = 6700

result = binary_search(numbers2, target)
print(
    f"Индекс элемента {target}: {result}, длинна списка = {len(numbers2)}, индекс первого элемента = {numbers.index(1)}")
