summa = int(input("Сумма:"))
hour = int(input("Текущий час:"))
if hour >= 10 and hour <= 12:
    print(summa/2)
else:
    print("Скидки нет")
    if hour >= 20 and hour <= 22:
        print(summa/4)
    else:
        print("Скидки нет")
if hour < 8 or hour > 22:
    print("Закрыто")
