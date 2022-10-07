# first_string = input()
# second_string = input()
# first_text = list(first_string)
# second_text = list(second_string)
# store = ""
# for i in range(0,len(second_string)):
#     first_text[i] = second_text[i]
#     check = ("".join(first_text))
#     if store != check:
#         print("".join((first_text)))
#     store = check


first_string = input()
second_string = input()

last_printed_string = first_string
for character_index in range(len(first_string)):
    left_part = second_string[:character_index + 1]
    right_part = first_string[character_index+1:]
    current_string = left_part + right_part
    if current_string == last_printed_string:
        continue
    print(current_string)
    last_printed_string = current_string

