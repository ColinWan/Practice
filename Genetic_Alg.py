import random
import string

target = 'Try this for fun'
pool = []
size = 200
mutation_rate = 0.2

def fitness(x):
    score = 0
    for i in range(len(target)):
        score += target[i] == x[i]
    return score

def prob(lst):
    sum = 0
    for item in lst:
        sum += item[1]
    for item in lst:
        item.append(item[1]/sum)
    return [lst, sum == 0]


def new_gen(pool, check):
    if not check:
        pool = []
        for i in range(size):
            temp = ''.join([random.choice(string.ascii_letters + string.digits + '')
                            for n in range(len(target))])
            pool.append([temp, fitness(temp)])
        [pool, temp] = prob(pool)

    new_pool = []
    for i in range(size):
        a = random.random()
        b = random.random()
        ind1 = 0
        ind2 = 0
        while a > 0:
            a -= pool[ind1][2]
            ind1 += 1
        while b > 0:
            b -= pool[ind2][2]
            ind2 += 1
        mom = pool[ind1-1][0]
        dad = pool[ind2-1][0]
        temp = ''.join([mom[:len(target)//2], dad[len(target)//2:]])
        if random.random() < mutation_rate:
            ind = int(random.uniform(0, 1) * len(target) // 1)
            temp = temp[0:ind] + random.choice(string.ascii_letters+' ') + temp[ind+1:]
        new_pool.append([temp, 2**fitness(temp)])
    return new_pool


def finished(x):
    result = False
    i = 0
    while not result and i < len(x):
        result = (x[i][0] == target or result)
        i += 1
    return result

def best(x):
    index = 0
    fit = 0
    for i in range(len(x)):
        if x[i][1] > fit:
            index = i
            fit = x[i][1]
    return x[index]

for i in range(size):
    temp = ''.join([random.choice(string.ascii_letters + string.digits+' ') for n in range(len(target))])
    pool.append([temp, 2**fitness(temp)])

num_gen = 0
while not finished(pool):
    num_gen += 1
    pro = prob(pool)
    print(best(pool))
    new_pool = new_gen(pool, pro)
    pool = new_pool
print(best(pool), num_gen)
