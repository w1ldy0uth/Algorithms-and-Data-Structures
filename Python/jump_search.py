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
    mas = list(map(int, input("Введите массив: ").split()))
    guess = int(input("Введите число, которое необходимо найти: "))
    print(int(jumpsearch(mas, guess, len(mas))))
