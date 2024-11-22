import random
import time

arr = [random.randint(1, 10000) for _ in range(1000000)]

def bubble_sort_descending(arr):
    n = len(arr)
    for k in range(n):
        for l in range(0, n-k-1):
            if arr[l] < arr[l+1]:
                arr[l], arr[l+1] = arr[l+1], arr[l]
    return arr

bubble_start_time=time.time()

bubble_sort_descending(arr)

bubble_end_time=time.time()

print(f"Время выполнения методом пузырьком: {bubble_end_time-bubble_start_time:.3f} секунд")


def selection_sort_descending(arr):
    for i in range(len(arr)):
        max_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]
    return arr

selection_start_time=time.time()

selection_sort_descending(arr)

selection_end_time = time.time()

print(f"Время сортировки выбором: {selection_end_time - selection_start_time:.3f} секунд")
