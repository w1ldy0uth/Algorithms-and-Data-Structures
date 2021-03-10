def eratosfen(n):
    nums = list(range(2, n+1))
    for num in nums:
        if num != 0:
            for i in range(2*num, n+1, num):
                nums[i-2] = 0

    for num in nums:
        if num != 0:
            print(num, end=" ")
    print()


if __name__ == '__main__':
    n = int(input("Enter a single number: "))
    eratosfen(n)
