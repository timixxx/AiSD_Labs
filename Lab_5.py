import random
import time

arr = []
print("Выберите размер массива:", "1 - 100", "2 - 500", "3 - 1000", "4 - 10000", sep="\n")
type = int(input())
if type == 1:
    n = 100
elif type == 2:
    n = 500
elif type == 3:
    n = 1000
elif type == 4:
    n = 10000


def fill(array):
    for i in range(n):
       array.append(random.randint(-50, 50))


fill(arr)


def LinearSearch(arr, element):
    for i in range (len(arr)):
        if arr[i] == element:
            return i
    return -1


t_start = time.time()
print("Результат линейного поиска:", LinearSearch(arr,13))
t_end = time.time()
print(t_end-t_start, "=> Линейный поиск")

def selectionSort(arr):
    for i in range(len(arr)):
	    min_idx = i
	    for j in range(i + 1, len(arr)):
		    if arr[min_idx] > arr[j]:
			    min_idx = j
	    arr[i], arr[min_idx] = arr[min_idx], arr[i]

selectionSort(arr)
#for i in range(n):
#    print(arr[i])

def BinarySearch(arr, val):
    first = 0
    last = len(arr)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if arr[mid] == val:
            index = mid
        else:
            if val<arr[mid]:
                last = mid -1
            else:
                first = mid +1
    return index

t_start = time.time()
print("Результат бинарного поиска:", BinarySearch(arr,13))
t_end = time.time()
print(t_end-t_start, "=> Бинарный поиск")


t_start = time.time()
print("Результат линейного поиска:", LinearSearch(arr,13))
t_end = time.time()
print(t_end-t_start, "=> Линейный поиск в отсортированном массиве")


