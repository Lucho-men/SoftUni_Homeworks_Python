cake_width = int(input())
cake_lenght = int(input())
entry = input()
cake_pieces_left = cake_lenght * cake_width

while entry != "STOP" and cake_pieces_left > 0:
    taken_pieces = int(entry)
    cake_pieces_left -= taken_pieces
    if cake_pieces_left <= 0:
        break
    entry = input()

if entry == "STOP":
    print(f"{cake_pieces_left} pieces are left.")

if cake_pieces_left < 0:
    print(f"No more cake left! You need {abs(cake_pieces_left)} pieces more.")
