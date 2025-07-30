import random

print(random.uniform(1, 10))
print(random.randint(1, 10))
print(random.randrange(1, 10))

l = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print(random.choice(l))
print(random.sample(l, 5))
print(random.choices(l, k=5))
random.shuffle(l)
print(l)

random.seed(1)
print(random.randint(1, 10))
print(random.random())
random.seed(1)
print(random.randint(1, 10))
print(random.random())

# secrets module for generating secure random numbers (tokens, passwords, etc.))
import secrets

print(secrets.randbelow(10))
print(secrets.randbits(4))
print(secrets.choice(l))
print(secrets.token_urlsafe(16))

# numpy random
import numpy as np

print(np.random.rand(3, 3))
print(np.random.randint(1, 10, 2))
print(np.random.randint(1, 10, (3, 3)))

array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
np.random.shuffle(array)
print(array)

np.random.seed(1)
print(np.random.randint(2, 12))
np.random.seed(1)
print(np.random.randint(2, 12))