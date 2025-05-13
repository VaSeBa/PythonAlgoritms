# Быстрая сортировка

arr = [243, -27, 145, 194, 389, 449, 434, 142, 134, 415]
print(arr)


def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i < pivot]
        greater = [i for i in array[1:] if i > pivot]
        print(f" pivot = {pivot}, less = {less}, greater = {greater}")

        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort(arr))
