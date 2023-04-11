name = input("Введите ФИО:")
name_split = name.split()
new_name = name_split[0] + " "
for i in range(1, len(name_split)):
    new_name += name_split[i][0] + "."
    if i != len(name_split) - 1:
        new_name += " "
print(new_name)