while True:
    text = ""
    command = input()
    if command == "End":
        break
    elif command == "SoftUni":
        continue
    else:
        for i in range(0,len(command)):
            text += (command[i] * 2)
        print(text)
