def bubblesort(arr):
    for i in range(len(arr)-1):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


if __name__ == "__main__":
    arr = list(map(int, input("Enter an unsorted array: ").split()))
    bubblesort(arr)
    print(arr)
