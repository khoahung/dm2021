import math
cluter1 = [(4, 6), (7, 4), (3, 5),(3, 9),(8, 5)]
cluter2 = [(5, 6), (7, 8), (5, 5),(3, 6),(7, 5)]
distance = 0
minimum = math.sqrt(pow((cluter1[0][0]-cluter2[0][0]), 2) + pow((cluter1[0][1]-cluter2[0][1]), 2))
maximum = math.sqrt(pow((cluter1[0][0]-cluter2[0][0]), 2) + pow((cluter1[0][1]-cluter2[0][1]), 2))
for i in cluter1:
    for j in cluter2:
        distance = math.sqrt(pow((i[0]-j[0]), 2) + pow((i[1]-j[1]), 2))
        print(round(distance,2), end='   ')
        if maximum < distance:
            maximum = distance;
        if minimum > distance:
            minimum = distance;
    print('            ')
print('max: {}'.format(round(maximum, 2)))
print('min: {}'.format(round(minimum, 2)))
