import random
import time

array = []
n = int(input("Введите размер массива: "))


def add(array):
    for i in range(n):
       array.append(random.randint(-50, 50))


#-----bubble sort-----#
def bubbleSort(arr):
	n = len(arr)
	for i in range(n-1):
		for j in range(0, n-i-1):
			if arr[j] > arr[j + 1] :   #swap if the element is greater then the next
				arr[j], arr[j + 1] = arr[j + 1], arr[j]


add(array)

t_start = time.time()
bubbleSort(array)
t_end = time.time()

print(t_end-t_start, "=> Bubble Sort" )


#-----Selection Sort-----#
def selectionSort(arr):
	for i in range(len(arr)):
		min_idx = i
		for j in range(i + 1, len(arr)):  #find the minimum element in unsorted array
			if arr[min_idx] > arr[j]:
				min_idx = j
		arr[i], arr[min_idx] = arr[min_idx], arr[i] #then swap minimum element with the first in array


array = []
add(array)

t_start = time.time()
selectionSort(array)
t_end = time.time()

print(t_end-t_start, "=> Selection Sort" )


#------Quick sort------#
def partition(arr, low, high):
	i = (low-1)
	pivot = arr[high]
	for j in range(low, high):
		if arr[j] <= pivot:
			i = i+1
			arr[i], arr[j] = arr[j], arr[i]
	arr[i+1], arr[high] = arr[high], arr[i+1]
	return (i+1)

def quickSort(arr, low, high):
	if len(arr) == 1:
		return arr

	if low < high:
		pi = partition(arr, low, high)
		quickSort(arr, low, pi-1)
		quickSort(arr, pi+1, high)

array = []
add(array)

t_start = time.time()
quickSort(array, 0, n-1)
t_end = time.time()

print(t_end-t_start, "=> Quick Sort" )

#for i in range(len(array)):
#	print(array[i])



