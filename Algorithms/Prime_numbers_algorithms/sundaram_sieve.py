def sundaram(n):
    new_n = int((n - 1) / 2)
    form_arr = [0] * (new_n + 1)

    for i in range(1, new_n + 1):
        j = i
        while (i + j + 2 * i * j) <= new_n:
            form_arr[i + j + 2 * i * j] = 1
            j += 1

    if n > 2:
        print(2, end=" ")

    for i in range(1, new_n + 1):
        if form_arr[i] == 0:
            print(2 * i + 1, end=" ")
    print()


if __name__ == '__main__':
    n = int(input("Enter a single number: "))
    sundaram(n)
