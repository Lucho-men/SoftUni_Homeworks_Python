free_space_width = int(input())
free_space_length = int(input())
free_space_height = int(input())
free_volume = free_space_height * free_space_length * free_space_width
box_volume = 1
current_box_volume = 0

entry = input()

while entry != "Done":
    number_of_boxes = int(entry)
    current_box_volume = number_of_boxes * box_volume
    free_volume -= current_box_volume
    if free_volume <= 0:
        print(f"No more free space! You need {abs(free_volume)} Cubic meters more.")
        break
    entry = input()

if entry == "Done":
    print(f"{free_volume} Cubic meters left.")

