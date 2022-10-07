floors = int(input())
rooms = int(input())

for i in range(floors, 0, -1):
    for j in range(0, rooms):
        if i % 2 != 0:
            if i == floors:
                print(f"L{i}{j}",end=" ")
            else:
                print(f"A{i}{j}",end=" ")
        else:
            if i == floors:
                print(f"L{i}{j}",end=" ")
            else:
                print(f"O{i}{j}",end=" ")
    print("")