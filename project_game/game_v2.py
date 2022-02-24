""" Игра угадай число"""
""" Компьютер сам загадывает и угадывает число"""

from black import main
import numpy as np 
def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загадываем число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    while True:
        count+=1
        predict_number = np.random.randint(1, 101) # Предпологаемое число
        if number == predict_number:
            break # Выход из цикла, когда угадали число
    return(count)


def score_game(random_predict) -> int:
    """За каком количество подходов в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict (_type_): Функция угадвания

    Returns:
        int: Среднее количество попыток
    """
    
    count_ls = [] # Список для сохранения количества попыток
    np.random.seed(1) # Фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # Загадали список чисел
    for number in random_array:
        count_ls.append(random_predict(number)) 
    score = int(np.mean(count_ls)) # находим среднее количество попыток
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток') 
    return(score)
print(f'Компьютер угадал число за {random_predict()} попыток')

# RUN

if __name__ == '__main__':
    score_game(random_predict)

    
 