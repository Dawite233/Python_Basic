# The classes a student is registered for 
classes_registered = ['ITEC 1150', 'ITEC 1100', 'ITEC 2150', 'ENGL 1340', 'MATH 1100']

# Make a list of only the itec classes 

only_itec = [ c for c in classes_registered if c.startswith('ITEC') ]
print(only_itec)

# Record temperature every day. Record -1 if not possible to take measurement.
high_temp = [-1, 78, 72, 67, -1, 51, 87, 82, -1, 54, 67, 78, -1, 70, -2]


# Make a list of onlu number that represent a valid temperature measurement
only_real_measurement = [ temp for temp in high_temp if temp != -1 ]
print(only_real_measurement)

temp_celsius = [ (temp_f -32 ) * 5 / 9 for temp_f in only_real_measurement ]
print(temp_celsius)

average = sum(temp_celsius) / len(temp_celsius)
print(f'The average is {average:.2f}C!')


numbers = [2, 4, 6 ]
plus_one = [n+1 for n in numbers ]
print(plus_one)


numbers = [0, 9, 0, 3, 4, 6, 0, 2]
numbers_no_zeros = [n for n in numbers if n != 0 ]
print(numbers_no_zeros)