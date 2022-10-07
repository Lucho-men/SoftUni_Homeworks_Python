text = input()
current_letter = ""
sum = 0

for i in range(0, len(text)):
    current_letter = text[i]
    if current_letter == "a":
        sum += 1
    elif current_letter == "e":
        sum += 2
    elif current_letter == "i":
        sum += 3
    elif current_letter == "o":
        sum += 4
    elif current_letter == "u":
        sum += 5

print(sum)