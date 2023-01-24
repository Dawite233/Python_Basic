# Tuples

city_state = [ ('Seattle', 'WA'), ('Portland', 'OR'), ('San Francisco', 'CA'), ('Minneapolis', 'MN') ]
print(len(city_state))

first_city_state = city_state[0]
print(first_city_state)

print(first_city_state[0])
print(first_city_state[1])

city, state = first_city_state
print(city)
print(state)

animals = ('Lion', 'Puma', 'Tiger', 'Elephant' )

lion, puma, tiger, elephant = animals
print(puma)
print(lion + ' is the king of the jungle.')


