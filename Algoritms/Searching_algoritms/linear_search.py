def linearsearch(array, item):
    for i in range(len(array)):
        if array[i] == item:
            return i

    return None


if __name__ == "__main__":
    arr = list(map(int, input("Enter an array: ").split()))
    guess = int(input("Enter a number to find: "))
    print(linearsearch(arr, guess))
