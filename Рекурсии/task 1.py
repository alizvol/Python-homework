def print_name(name1, name2, name3):
    while name1 or name2 or name3 != "None":
        name1 = input("name1:")
        name2 = input("name2:")
        name3 = input("name3:")
        print(name1, name2, name3)
        if name1 or name2 or name3 == "None":
            break
print_name("a","b","c")