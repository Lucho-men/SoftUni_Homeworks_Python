number_of_strings = int(input())

for i in range(number_of_strings):
    is_pure = True
    string = input()
    for j in range(0,len(string)):
        if string[j] == "," or string[j] == "." or string[j] == "_":
            is_pure = False
            break
    if is_pure == False:
        print(f"{string} is not pure!")
    else:
        print(f"{string} is pure.")


