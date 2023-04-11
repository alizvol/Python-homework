fun = input("Введите раздел:")
if fun == "game":
    print("Угадай число")
    for i in range(3):
        game = input("Угадай число (off - завершить):")
        if i == 5:
            print("Вы выиграли билет на концерт!")
            if game == "off":
                break
