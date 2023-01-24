# useful for returning multiple values from a function 

def get_random_cat_pattern():
    return 'tiger', 'stripes' # return a tuple 


# Unpack yuo tuple to conveniently get both values in sepatate variable 
cat, pattern = get_random_cat_pattern()

# if you prefer you can do this but ut is ussually more work 
data =get_random_cat_pattern

try:
    print(data[10]) # tiger
except: 
    print('oops. that does not exist.')