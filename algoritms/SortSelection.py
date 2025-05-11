# сортировка выбором - на основе поиска минимального значения
from algoritms.smallest_element import find_min_number


def selection_sort(array):
    new_arr = []
    for i in range(len(array)):
        smallest, index = find_min_number(array)
        new_arr.append(array.pop(index))
    return new_arr


arr = [79, 13, 12, 44, 14, -2, -67, 9, 80, -77]
print(arr)

new_arr = selection_sort(arr)
print(new_arr)
