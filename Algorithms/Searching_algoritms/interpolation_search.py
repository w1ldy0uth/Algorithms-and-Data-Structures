def intplsearch(array, size, item):
    low = 0
    mid = 0
    high = len(array) - 1

    while (array[low] < item) and (array[high] > item):
        if array[high] == array[low]:
            break
        mid = int(low+((item-array[low])*(high-low))/(array[high]-array[low]))

        if array[mid] < item:
            low = mid + 1
        elif array[mid] > item:
            high = mid - 1
        else:
            return mid

    if array[low] == item:
        return low
    if array[high] == item:
        return high

    return None


if __name__ == "__main__":
    arr = list(map(int, input("Enter a sorted array: ").split()))
    guess = int(input("Enter a number to find: "))
    print(intplsearch(arr, guess))
