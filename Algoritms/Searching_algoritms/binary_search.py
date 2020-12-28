def binsearch(array, item):
    low = 0
    high = len(array)-1

    while low <= high:
        mid = (low + high) // 2
        it = array[mid]
        if it == item:
            return mid
        if it > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


if __name__ == "__main__":
    arr = list(map(int, input("Enter a sorted array: ").split()))
    guess = int(input("Enter a number to find: "))
    print(binsearch(arr, guess))
