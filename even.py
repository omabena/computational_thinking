import random

def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    x = int(random.uniform(0,100))
    if x % 2 == 1:
        return x-1
    else:
        return x

even_gen = []
for i in range(0,10000):
    even_gen.append(genEven())

# print(even_gen)


def genEvenGenerator(a, b):
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    x = random.randint(a, b)

    if x%2 == 0:
       yield x
    else:
       yield from genEvenGenerator(a, b)

for each in range(10):
    print(next(genEvenGenerator(0,100)))