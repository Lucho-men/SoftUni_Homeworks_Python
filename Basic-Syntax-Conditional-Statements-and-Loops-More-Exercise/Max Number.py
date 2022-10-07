import sys
max_num = - sys.maxsize

while True:
    line = input()
    if line == "Stop":
        break
    else:
        current_num = int(line)
        if current_num > max_num:
            max_num = current_num

print(f"{max_num}")