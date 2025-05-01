from functools import reduce

lst = [1,2,3,4,5,6,7]

# Map will take first argument as function and second argument as iterables
# Maps are useful when we want to perform common action on all values of iterables
sqr_lst = list(map(lambda val: val*val, lst))
print(sqr_lst)

# filter will be useful to filter out based on condition
even_lst = list(filter(lambda val: val % 2 == 0, lst))
print(even_lst)

# reduce will be useful to perform rolling action on given iterable
sum_val = reduce(lambda val1, val2: val1+val2, lst)
print(sum_val)
