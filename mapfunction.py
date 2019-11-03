from functools import reduce
def normalize(names):
    for name in names:
        name.upper()
        return names
l1 = ['adam', 'lisa', 'barT' ]
l2 = normalize(l1)
print(l2)