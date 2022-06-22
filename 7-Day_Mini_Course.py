# LESSON ONE

# Original List
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd = x[::2]
even = x[1::2]

backward_odd = x[-2::-2]
backward_even = x[-1::-2]

short_list = x[-4:-9:-2]

#print(short_list)

# LESSON TWO

price1 = {
    'apple' : 1.5,
    'orange' : 1.25,
    'strawberry' : 1.0
}
price2 = {
    'banana' : 0.5
}
pairs1 = list(price1.items())
pairs2 = list(price2.items())
price = dict(pairs1 + pairs2)
#print(price)

price = {**price1, **price2}

#print(price)

price = price1 | price2

#print(price)

# LESSON THREE

x = [("gamma", 0.1), ("alpha", -3), ("beta", 1.1), ("alpha", 0.5, 1)]

#print(x)

# Corrected from sorted(x), which does not seem to work with tuples.
x.sort()

# sort() seems to order by the first element first and then orders by the second and
# onward. Having more elements does not affect the sort. Strings are ordered
# alphabetically.
#print(x)

# LESSON FOUR

coord = {"lat": 51.5072, "lon": -0.1276}
print("latitude %(lat)f, longitude %(lon)f" % coord)
print("latitude {lat}, longitude {lon}".format(**coord))
print(f'latitude {coord["lat"]: 0.2f}, longitude {coord["lon"]: 0.2f}')