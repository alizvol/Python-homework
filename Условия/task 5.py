number = int(input("Введите число:"))
last = number % 10
summa = sum([number])
if last % 2 == 0 and summa % 3 == 0:
    print("Делится")
else:
    print("Не делится")