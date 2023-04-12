towar1 = int(input("Введите сумму 1 товара:"))
towar2 = int(input("Введите сумму 2 товара:"))
towar3 = int(input("Введите сумму 3 товара:"))
summa = towar1 + towar2 + towar3
if towar1 < towar2 and towar2 < towar3:
    print(summa/2)
if towar1 > towar2 and towar2 > towar3:
        print(summa/3)
if towar1 < towar2 and towar2 < towar3 or towar1 > towar2 and towar2 > towar3:
    print("Акция!")
else:
    print("К оплате:")
