def max_chiclo(b, c):
    a = int(input("Введите число a: "))

    if a > 0:
        maxsimum = max(a, b, c)
        return maxsimum
    else:
        return -1

b = int(input("Введите число b: "))
c = int(input("Введите число c: "))

print("Результат:", max_chiclo(b, c))