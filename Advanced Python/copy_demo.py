import copy

a = [[1, 2], [3, 4]]
b = copy.copy(a)
# list.copy() works same & its shallow copy
# list(iterable) works same & its shallow copy)
# list[:] works same & its shallow copy)
b[0][0] = 99
print(a)  # [[99, 2], [3, 4]] ← inner object is shared!

# Deep copy
a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)
b[0][0] = 99
print(a)  # [[1, 2], [3, 4]] ← fully independent copy!

# copy.copy() for dict
data = {'a': {'x': 1, 'y': 2}, 'b': 2, 'c': 3}
copied_data = copy.copy(data)  # or data.copy()
copied_data['a']['x'] = 99
print(
    data)  # {'a': {'x': 99, 'y': 2}, 'b': 2, 'c': 3} ← inner object is shared!

data = {'a': {'x': 1, 'y': 2}, 'b': 2, 'c': 3}
copied_data = copy.deepcopy(data)
copied_data['a']['x'] = 99
print(
    data)  # {'a': {'x': 1, 'y': 2}, 'b': 2, 'c': 3} ← fully independent copy!

# copy.copy() for class


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Company:

    def __init__(self, name, employees):
        self.name = name
        self.employees = employees


p = Person('John', 30)
c = Company('ABC', [p])

c1 = copy.copy(c)
c1.name = 'DEF'
c1.employees[0].name = 'Jane'
print(c.employees[0].name)  # Jane ← inner object is shared!

c2 = copy.deepcopy(c)
c2.name = 'GHI'
c2.employees[0].name = 'Tom'
print(c.employees[0].name)  # Jane ← fully independent copy!