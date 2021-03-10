import random


def bubblesort(arr):
    for i in range(len(arr)-1):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


if __name__ == "__main__":
    n = int(input("Enter an array length: "))
    arr = [random.randint(-100, 100) for i in range(n)]
    print(arr)
    bubblesort(arr)
    print(arr)
