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
    mas = list(map(int, input("Введите массив: ").split()))
    guess = int(input("Введите число, которое необходимо найти: "))
    print(exponsearch(mas, guess))
