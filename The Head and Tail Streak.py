import random, time

no_of_steaks=0

for x in range(10000):
    ision = []
    for y in range(100):
        dess = random.randint(0, 1)
        if dess == 0:
            ision.append('H')
        else:
            ision.append('T')

    for z in range(95):
        if ision[z:z+6] == ['H', 'H', 'H', 'H', 'H', 'H'] or ision[z:z+6] == ['T', 'T', 'T', 'T', 'T', 'T']:
            no_of_steaks += 1
    
print(no_of_steaks)
plus = (no_of_steaks / (10000*(100/6)))*100
print(plus)
