def atkin(limit):
    if limit > 2:
        print(2, end=" ")
    if limit > 3:
        print(3, end=" ")

    sieve = [False] * limit
    for i in range(0, limit):
        sieve[i] = False

    x = 1
    while x ** 2 < limit:
        y = 1
        while y ** 2 < limit:
            num = 4 * x ** 2 + y ** 2
            if num <= limit and (num % 12 == 5 or num % 12 == 1):
                sieve[num] ^= True
            num = 3 * x ** 2 + y ** 2
            if num <= limit and num % 12 == 7:
                sieve[num] ^= True
            num = 3 * x ** 2 - y ** 2
            if x > y and num <= limit and num % 12 == 11:
                sieve[num] ^= True
            y += 1
        x += 1

    sq = 5
    while sq ** 2 < limit:
        if sieve[sq]:
            for i in range(sq ** 2, limit, sq ** 2):
                sieve[i] = False
        sq += 1

    for num in range(5, limit):
        if sieve[num]:
            print(num, end=" ")
    print()


if __name__ == '__main__':
    lim = int(input("Enter a single number: "))
    atkin(lim)
