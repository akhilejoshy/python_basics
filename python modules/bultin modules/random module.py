import random

print(random.randint(10,20))

print(random.uniform(10,20))

itm=['a','b','c','d']
print(random.choice(itm))

print(random.sample(itm,2))

random.shuffle(itm)
print(itm)