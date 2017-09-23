pizzas = ['Cheese','Pepperoni','Mushroom']
friend_pizzas = pizzas[:]
pizzas.append('Pesto')
friend_pizzas.append('Meatball')
print("My favourite pizzas are: ")
for x in pizzas:
    print("\t-" + str(x))
print("\nMy friend's favourite pizzas are: ")
for y in friend_pizzas:
    print("\t-" + str(y))

