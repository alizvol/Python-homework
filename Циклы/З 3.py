login = input("Введите логин")
block = "=?*^$№@_"
for i in block:
    if i in login:
        print(i)
    else:
        print(" ")
