# adding the values with common key
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
# output= {'a': 400, 'b': 400, 'd': 400, 'c': 300}

for key in d2:
    if key in d1:
        d2[key] = d2[key] + d1[key]
    else:
        pass

print(d2)
