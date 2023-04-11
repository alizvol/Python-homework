a = input("Введите почту:")
b = a.find("@")
if b != -1:
    print(a[0:b])