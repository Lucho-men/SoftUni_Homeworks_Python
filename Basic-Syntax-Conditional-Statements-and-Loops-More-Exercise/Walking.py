target_steps_for_the_day = 10000
entry = input()
total_steps = 0
current_steps = 0

while entry != "Going home":
    current_steps = int(entry)
    total_steps += current_steps
    if total_steps >= target_steps_for_the_day:
        break
    entry = input()


if entry == "Going home":
    steps_to_home = int(input())
    total_steps = total_steps + steps_to_home

if total_steps >= target_steps_for_the_day:
    print(f"Goal reached! Good job!")
    print(f"{abs(total_steps - target_steps_for_the_day)} steps over the goal!")
else:
    print(f"{target_steps_for_the_day - total_steps} more steps to reach goal.")
