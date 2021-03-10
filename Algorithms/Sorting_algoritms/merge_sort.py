import random


def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        mergesort(left)
        mergesort(right)

        idx = 0
        jdx = 0
        kdx = 0

        while idx < len(left) and jdx < len(right):
            if left[idx] < right[jdx]:
                arr[kdx] = left[idx]
                idx += 1
            else:
                arr[kdx] = right[jdx]
                jdx += 1
            kdx += 1

        while idx < len(left):
            arr[kdx] = left[idx]
            idx += 1
            kdx += 1

        while jdx < len(right):
            arr[kdx] = right[jdx]
            jdx += 1
            kdx += 1


if __name__ == '__main__':
    n = int(input("Enter an array length: "))
    arr = [random.randint(-100, 100) for i in range(n)]
    print(arr)
    mergesort(arr)
    print(arr)
