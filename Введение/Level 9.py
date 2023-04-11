chislo = int(input("Введите число:"))
a = chislo % 100 % 10
b = chislo // 10 % 10
c = chislo // 100 % 10
print(a, b, c)