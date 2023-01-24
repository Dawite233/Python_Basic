def get_distance():
    miles = 1000
    km = miles * 1.6
    return miles, km


distances = get_distance()
print(distances[0])
print(distances)


miles, km = get_distance()
print(miles)
print(km)