import numpy as np

def random_predict(number) -> int:
    """Высчитываем рандомное число

    Args:
        number (int, optional): Искомое число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0
    min = 1
    max = 101
    
    random_number = np.random.randint(min, max) # случайное число в диапазоне
    
    while True:
        count += 1 # счетчик попыток
    
        number = round((min+max) / 2) # округленное среднее значение диапазона
    
        if number > random_number:
            max = number # двигаем максимальную границу
    
        elif number < random_number:
            min = number # двигаем минимальную границу

        else:
            print(f"Компьютер угадал число за {count} попыток. Это число {number}")
            break #конец игры выход из цикла
        
    return(count)


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
score_game(random_predict)