budget = float(input())
price_per_1_kg_of_flower = float(input())
price_for_one_pack_of_eggs = 0.75 * price_per_1_kg_of_flower
price_for_milk = (price_per_1_kg_of_flower * 1.25) / 4
price_for_bread = price_per_1_kg_of_flower + price_for_one_pack_of_eggs + price_for_milk
bread_count = 0
colored_eggs_counter = 0

while budget >= price_for_bread:
    budget -= price_for_bread
    bread_count += 1
    colored_eggs_counter += 3
    if bread_count % 3 == 0:
        colored_eggs_counter -= bread_count - 2
print(f"You made {bread_count} loaves of Easter bread! Now you have {colored_eggs_counter} eggs and {budget:0.2f}BGN left.")


