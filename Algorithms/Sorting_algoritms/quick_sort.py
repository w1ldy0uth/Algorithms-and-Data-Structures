import random


def partition(arr, start, end):
    pivot = arr[start]
    low = start + 1
    high = end

    while True:
        while low <= high and arr[high] >= pivot:
            high -= 1

        while low <= high and arr[low] <= pivot:
            low += 1

        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
        else:
            break

    arr[start], arr[high] = arr[high], arr[start]

    return high


def quicksort(arr, start, end):
    if start >= end:
        return

    p = partition(arr, start, end)
    quicksort(arr, start, p-1)
    quicksort(arr, p+1, end)


if __name__ == '__main__':
    n = int(input("Enter an array length: "))
    arr = [random.randint(-100, 100) for i in range(n)]
    print(arr)
    quicksort(arr, 0, len(arr)-1)
    print(arr)
