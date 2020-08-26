import random
def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    # Your code here
    x = int(random.uniform(10,21))
    if x % 2 == 1:
        return x-1
    else:
        return x


even_gen = []
for i in range(0,10):
    even_gen.append(stochasticNumber())

print(even_gen)