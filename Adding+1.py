numbers = [2, 4, 6, ]
plus_0ne = [ n+1 for n in numbers]
multiple = [ n*2 for n in numbers]
print(multiple)
print(plus_0ne)


numbers = [0, 9, 0, 3, 4, 6, 0, 2]
numbers_no_zeros = [ n for n in numbers if n != 0 ]
print(numbers_no_zeros)

numbers_doubled_no_zeros = [ n * 2 for n in numbers if n!=0 ]
print(numbers_doubled_no_zeros)