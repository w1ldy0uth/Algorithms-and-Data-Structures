def linearsearch(array, item):
    for i in range(len(array)):
        if array[i] == item:
            return i

    return None

if __name__ == "__main__":
    mas = list(map(int, input("Введите массив: ").split()))
    guess = int(input("Введите число, которое необходимо найти: "))
    print(linearsearch(mas, guess))
