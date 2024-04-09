"""Игра угадай число.
Компьютер сам загадывает и угадывает число
"""

import numpy as np

def random_predict(number:int=1) -> int:
# Обратите внимание, что в аргументах функции мы через двоеточие указываем тип данных для ввода (int), 
# через равно — стандартное значение этого типа данных. 
# Стрелка (->) указывает, какой тип данных мы должны получить на выходе. 
# Это упростит заполнение документации (VS Code сможет автоматически генерировать её), 
# а также позволит в дальнейшем эффективнее работать с ошибками

    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0
    
    while True:
        count +=1 
        predict_number = np.random.randint(1,101)   # предполагаемое число
        if number == predict_number:
            break # выход из цикла, если угадали
    return count

# print(f'Количество попыток: {random_predict()}')

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания
        
    Returns:
        int: среднее количество попыток
    """
    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1,101, size=(1000)) # загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls)) # находим среднее количество попыток
    
    print('Ваш алгоритм угадывает число в среднем за: {} попыток'.format(score))
    return score

if __name__ == '__main__':
    # RUN
    score_game(random_predict)
    