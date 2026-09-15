from io import TextIOWrapper
import random
import time


def BubbleSort(array):
    for i in range(len(array)):
        ready = True
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                ready = False
        if ready:
            return array
    return array


def InsertionSort(array, l=0, r=0):
    if not r:
        r = len(array)-1
    for i in range(l+1, r):
        j, item = i-1, array[i]
        while j >= l and array[j] > item:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = item
    return array


def Merge(left_array, right_array):
    if not len(left_array):
        return right_array
    if not len(right_array):
        return left_array
    result_array = []
    i_left = i_right = 0
    while len(result_array) < len(left_array)+len(left_array):
        if left_array[i_left] < right_array[i_right]:
            result_array.append(left_array[i_left])
            i_left += 1
        else:
            result_array.append(right_array[i_right])
            i_right += 1
        if i_right == len(right_array):
            result_array += left_array[i_left:]
            break
        if i_left == len(left_array):
            result_array += right_array[i_right:]
            break
    return result_array


def MergeSort(array):
    if len(array) < 2:
        return array
    middle = len(array)//2
    return Merge(MergeSort(array[middle:]), MergeSort(array[:middle]))


def Quicksort(array):
    if len(array) < 2:
        return array
    left, middle, right = [], [], []
    key = array[random.randint(0, len(array)-1)]
    for item in array:
        if item < key:
            left.append(item)
        elif item == key:
            middle.append(item)
        elif item > key:
            right.append(item)
    return Quicksort(left) + middle + Quicksort(right)


def Timsort(array):
    if len(array) < 2:
        return array
    range_sort = 32
    for i in range(0, len(array), range_sort):
        InsertionSort(array, i, min(i+range_sort, len(array)))
    while range_sort < len(array):
        for i in range(0, len(array), range_sort*2):
            mid, end = i+range_sort, min(i+range_sort*2, len(array))
            array[i:end] = Merge(array[i:mid], array[mid:end])
        range_sort *= 2
    return array


# with open('DataStructuresAndAlgorithms/ArrayNumbersPower7.txt', "w+") as ANP:
#     array = [random.randint(0, 999) for _ in range(10**7)]
#     for num in array:
#         ANP.write(str(num) + ' ')

def timer(n, func):
    with open(f'DataStructuresAndAlgorithms/ArrayNumbersPower{n}.txt', "r+") as ANP:
        arr = list(map(int, ANP.read().split()))
    t0 = time.time()
    func(arr)
    t1 = time.time()
    print(f"Time execution function of {func.__name__:14} 10^{n}: {t1-t0:5f} sec")


for i in range(1, 8):
    print()
    for name in (BubbleSort, InsertionSort, MergeSort, Quicksort, Timsort):
        if i > 4 and name.__name__ in ('BubbleSort', 'InsertionSort'):
            continue
        else:
            timer(i, name)
