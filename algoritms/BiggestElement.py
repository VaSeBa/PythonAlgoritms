# поиск большего элемента массива

import random

array = [random.randint(-100, 500) for i in range(10)]
print(array)

def find_biggest(arr):
    biggest = arr[0]
    for i in arr:
        print(f"i = {i}")
        if i > biggest:
            biggest = i
            print(f"i = {i}, biggest = {biggest}")

find_biggest(array)