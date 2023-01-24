# if the number is greater than 0
numbers = [1, -10, 40, -6. -500, 350]
positive_numbers = [n for n in numbers if n >= 0 ]
print(positive_numbers) 


foods = ['cheese pizza', 'pepperoni pizza', 'ice cream', 'veggie pizza', 'tacos']
pizzas = [food for food in foods if 'pizza' in food]
print(pizzas)

# Remember that Python does not have contains() methods, use the in operator to see of a string contains substring, or a list contain an item

example = [1, 5, 10]
is_one_in_list = 1 in example 
is_seven_in_list = 7 in example

course = 'ITEC  1150 Programming Logic'
if '1150' in course:
    print('This is progrmming logic')
