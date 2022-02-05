'''Игра компьютер угадает число меньше чем за 20 попыток'''

import numpy as np

a = 1
b = 101

number = np.random.randint(a, b)

count = 0

while True:
    count+=1
    predict_number = np.random.randint(a, b)
    
    if predict_number > number:
        print("Число должно быть меньше")
        if predict_number > (number+9):
            print("как минимум на десяток")
            b = predict_number - 9
        else:
            b = predict_number - 1

    elif predict_number < number:
        print("Число должно быть больше")
        if predict_number < (number-9):
            print("как минимум на десяток")
            a = predict_number + 9
        else:
            a = predict_number + 1

    else:
        print(f"Вы угадали число за {count} попыток. Это число {number}")
        break #конец игры выход из цикла