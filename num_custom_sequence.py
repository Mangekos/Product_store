def print_custom_sequence(n):
    i = 1
    count = 1
    while count <= n:
        for _ in range(i):
            print(i, end='')
            count += 1
            if count > n:
                break
        i += 1


n = int(input("Введите число элементов на вывод: "))
print_custom_sequence(n)
