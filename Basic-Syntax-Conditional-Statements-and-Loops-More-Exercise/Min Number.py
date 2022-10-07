import sys
min_num = sys.maxsize

while True:
    line = input()
    if line == "Stop":
        break
    else:
        current_num = int(line)
        if current_num < min_num:
            min_num = current_num

print(f"{min_num}")