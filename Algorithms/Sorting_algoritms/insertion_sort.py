import random


def insertionsort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


if __name__ == "__main__":
    n = int(input("Enter an array length: "))
    arr = [random.randint(-100, 100) for i in range(n)]
    print(arr)
    insertionsort(arr)
    print(arr)
