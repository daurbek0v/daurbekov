'''Игра компьютер угадает число меньше чем за 20 попыток'''

import numpy as np



min = 1
max = 101

random_number = np.random.randint(min, max)

count = 0

while True:
    count+=1
    mid = round((min+max) / 2)
    
    if mid > random_number:
        max = mid
    
    elif mid < random_number:
        min = mid

    else:
        print(f"Компьютер угадал число за {count} попыток. Это число {random_number}")
        break #конец игры выход из цикла
    

