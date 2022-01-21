'''Игра угадай число меньше чем за 20 попыток'''

import numpy as np

number = np.random.randint(1, 101)

count = 0

while True:
    count+=1
    predict_number = int(input("Угадай число от 1 до 100: "))
    
    if predict_number > number:
        print("Число должно быть меньше")
        if predict_number > (number+10):
            print("как минимум на 10")
        
    elif predict_number < number:
        print("Число должно быть больше")
        if predict_number < (number-10):
            print("как минимум на 10")
        
    else:
        print(f"Вы угадали число за {count} попыток. Это число {number}")
        break #конец игры выход из цикла