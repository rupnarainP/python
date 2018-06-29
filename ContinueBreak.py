shopping_list = {"milk", "pasta", "eggs", "spam", "bread", "rice"}

for item in shopping_list:
    if item == "spam":
        print("skip spam")
        continue

    print("Buy: " + item)

meal = {"eg", "bacon", "spam", "sausages"}

for item in meal:
    if item == "spam":
        nasty_food_item = item
        break

if nasty_food_item:
    print("Can't buy anything with spam in it")