# Uppercase all food items, but only if its pizza

foods = ['cheese pizza', 'pepperoni pizza', 'ice cream', 'veggie pizza', 'tocos']
pizzas = [food.upper() for food in foods if 'pizza' in food ]
print(pizzas)


# equivalent, with loop adn if statement 
# Making upper case 

foods = ['cheese pizza', 'pepperoni pizza', 'ice cream', 'veggie pizza', 'tocos']
pizzas = []
for food in foods:
    if 'pizza' in food:
        uppercase_pizza = food.upper()
        pizzas.append(uppercase_pizza)
print(pizzas)