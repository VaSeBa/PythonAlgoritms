import random

# O(n). Это самый эффективный метод для поиска минимума
def find_min_number(arr):
    smallest_value = arr[0]
    index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest_value:
            smallest_value = arr[i]
            index = i
            print(f"Меньшее значение - {smallest_value}, под индексом - {index}")
    return smallest_value, index


# # arr = [random.randint(-100, 100) for i in range(10)]
# print(arr)

# find_min_number(arr)
