import math
cluter1 = [(4, 6), (7, 4), (3, 5)]
cluter2 = [(5, 6), (7, 8), (5, 5)]
distance = 0
min = math.sqrt(pow((cluter1[0][0]-cluter2[0][0]), 2) + pow((cluter1[0][1]-cluter2[0][1]), 2))
max = math.sqrt(pow((cluter1[0][0]-cluter2[0][0]), 2) + pow((cluter1[0][1]-cluter2[0][1]), 2))
for i in cluter1:
    for j in cluter2:
        distance = math.sqrt(pow((i[0]-j[0]), 2) + pow((i[1]-j[1]), 2))
        print(distance, end='                 ')
        if max < distance:
            max = distance;
        if min > distance:
            min = distance;
    print('            ')
print('max: {}'.format(max))
print('min: {}'.format(min))