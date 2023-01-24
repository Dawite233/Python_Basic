# if you are making a list from another list, you can use list comprejensions

strings = ['Pizza', 'Beyonce', 'Cat']
lengths = []

for string in strings:
    length = len(string)
    lengths.append(length)

print(lengths)
print(len(strings))

# The short version 
Strings = ['Pizza', 'Beyonce', 'Cat']
lengths = [len(string) for string in strings ]

print(lengths)