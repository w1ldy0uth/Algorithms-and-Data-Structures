import random


def selectionsort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


if __name__ == "__main__":
    n = int(input("Enter an array length: "))
    arr = [random.randint(-100, 100) for i in range(n)]
    print(arr)
    selectionsort(arr)
    print(arr)
