import itertools
a = [1, 1, 2]
b = []
sec = []
third = []
var = itertools.permutations(a)
for i in var:
    sec.append(list(i))
for x in sec:
    if x not in third:
        third.append(x)
print(third)