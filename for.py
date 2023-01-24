# Unordered collection
# Duplicates not allowed


cats = {'Leopard', 'Tiger', 'Cheetah'}
print(cats)

for cat in cats:
    print(cat)


# Adding and Removing
cats.add('Puma')
cats.remove('Cheetah')
print(cats)

cats.add('Puma') # no duplicates


# Seting
animals = set()

animals.add('Lion')
animals.add('Tiger')
animals.add('Cheetah')
animals.add('Elephant')
animals.add('Black cat')
animals.remove('Cheetah')
print(animals)

for animal in animals:
    print(animal)



bird_list = ['robin', 'swan', 'swan', 'eagle', 'cardinal', 'swan', 'robin']
bird_list_not_duplicated = list(set(bird_list))
print(bird_list_not_duplicated)

