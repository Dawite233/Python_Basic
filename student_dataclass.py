 # Rmoving any duplicates from a list 

myList = ['dawite', 'dawit', 'dawite', 'dawit', 'dawi', 'dawi', 'daw']
myList = list(dict.fromkeys(myList))
print(myList)

# Another way to remove any duplicates from a list

def my_function(D):
    return list(dict.fromkeys(D))

my_D = my_function(['dawite', 'dawit', 'dawite', 'dawit', 'dawi', 'dawi', 'daw'])
print(my_D)