def exponsearch(array, item):
    if array[0] == item:
        return 0
    if array[len(array)-1] == item:
        return 0

    rng = 1

    while (rng < len(array)) and (array[rng] <= item):
        rng *= 2

    for i in range(rng//2, rng):
        if array[i] == item:
            return i

    return None


if __name__ == "__main__":
    arr = list(map(int, input("Enter a sorted array: ").split()))
    guess = int(input("Enter a number to find: "))
    print(exponsearch(arr, guess))
