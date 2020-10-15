import math

def jumpsearch(array, item, size):
    jump = math.sqrt(size)

    prev = 0
    while array[int(min(jump, size)-1)] < item:
        prev = jump
        jump += math.sqrt(size)
        if prev >= size:
            return None

    while array[int(prev)] < item:
        prev += 1
        if prev == min(jump, size):
            return None

    if array[int(prev)] == item:
        return prev

    return None


if __name__ == "__main__":
    arr = list(map(int, input("Enter a sorted array: ").split()))
    guess = int(input("Enter a number to find: "))
    print(jumpsearch(arr, guess))
