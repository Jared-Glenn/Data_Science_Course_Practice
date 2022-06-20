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
print(price)

price = {**price1, **price2}

print(price)

price = price1 | price2

print(price)