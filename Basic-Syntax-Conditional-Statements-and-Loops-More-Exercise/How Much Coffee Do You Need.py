number_of_coffies = 0
while True:
    command = input()
    if command == "coding":
        number_of_coffies += 1
    elif command == "CODING":
        number_of_coffies += 2
    elif command == "cat":
        number_of_coffies += 1
    elif command == "CAT":
        number_of_coffies += 2
    elif command == "dog":
        number_of_coffies += 1
    elif command == "DOG":
        number_of_coffies += 2
    elif command == "movie":
        number_of_coffies += 1
    elif command == "MOVIE":
        number_of_coffies += 2
    elif command == "END":
        break
    else:
        continue

if number_of_coffies > 5:
    print("You need extra sleep")
else:
    print(number_of_coffies)
