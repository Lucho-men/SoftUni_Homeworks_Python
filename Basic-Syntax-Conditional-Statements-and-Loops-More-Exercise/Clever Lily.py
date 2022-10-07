age = int(input())
price_washing_machine = float(input())
price_per_toy = int(input())

money_from_bd = 0.0
numbe_of_toys = 0
money_from_toys = 0.0
total_money_collected = 0.0
count = 0
for i in range(1, age + 1):
    if i % 2 == 0:
        count += 1
        money_from_bd += (10.0 * count)
    else:
        numbe_of_toys += 1

money_from_toys = numbe_of_toys * price_per_toy
total_money_collected = money_from_toys + money_from_bd - (count * 1)

if total_money_collected >= price_washing_machine:
    print(f"Yes! {total_money_collected - price_washing_machine:0.2f}")
else:
    print(f"No! {price_washing_machine - total_money_collected:0.2f}")
