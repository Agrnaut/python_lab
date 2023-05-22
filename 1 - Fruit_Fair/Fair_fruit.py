from FruitStock import Fair
from FruitStock import Requester

print("Welcome to the All-Fruit-Fair")

requester = Requester(input("Type in your name:"))


file = open("Fruits.txt", "r")
stock = []

for fruit in file:

    fruit = fruit.strip().upper()
    stock.append(fruit)
file.close()
final_stock = Fair(stock)
x = len(stock)

for i in range(x):
    print ("{} [{}]".format(final_stock[i],i))

chosen_fruit = int(input("Pick a fruit according to the number on their side:"))
for choice in final_stock:
    if chosen_fruit >= x or chosen_fruit < 0:
        print("Invalid option")
        break
    else:
        print(f"Thanks for choosing our services, {requester.name} requested the fruit: {final_stock[chosen_fruit]}")
        break

