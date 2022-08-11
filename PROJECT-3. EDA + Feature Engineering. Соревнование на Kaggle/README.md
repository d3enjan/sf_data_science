# <center> <img src = https://yakutsk.ru/wp-content/uploads/2022/04/25/bcom-logo-df420e11291b4befab53dfbeb263f19e.jpg alt="drawing" style="width:400px;">

# <center> Проект: Построение модели, вычисляющей отели, которые накручивают себе рейтинг

## Оглавление
1. [Описание проекта](https://github.com/d3enjan/sf_data_science/tree/main/PROJECT-3.%20EDA%20%2B%20Feature%20Engineering.%20%D0%A1%D0%BE%D1%80%D0%B5%D0%B2%D0%BD%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%BD%D0%B0%20Kaggle#%D0%BE%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)
2. [Какой кейс решаем?](https://github.com/d3enjan/sf_data_science/tree/main/PROJECT-3.%20EDA%20%2B%20Feature%20Engineering.%20%D0%A1%D0%BE%D1%80%D0%B5%D0%B2%D0%BD%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%BD%D0%B0%20Kaggle#%D0%BA%D0%B0%D0%BA%D0%BE%D0%B9-%D0%BA%D0%B5%D0%B9%D1%81-%D0%BC%D1%8B-%D1%80%D0%B5%D1%88%D0%B0%D0%B5%D0%BC)
3. [Краткая информация о данных](https://github.com/d3enjan/sf_data_science/tree/main/PROJECT-3.%20EDA%20%2B%20Feature%20Engineering.%20%D0%A1%D0%BE%D1%80%D0%B5%D0%B2%D0%BD%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%BD%D0%B0%20Kaggle#%D0%BA%D1%80%D0%B0%D1%82%D0%BA%D0%B0%D1%8F-%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D1%8F-%D0%BE-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85)
4. [Этапы работы над проектом](https://github.com/d3enjan/sf_data_science/blob/main/PROJECT-1.%20%D0%90%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7%20%D0%B2%D0%B0%D0%BA%D0%B0%D0%BD%D1%81%D0%B8%D0%B9%20%D0%B8%D0%B7%20HeadHunter/README.md#%D1%8D%D1%82%D0%B0%D0%BF%D1%8B-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B-%D0%BD%D0%B0%D0%B4-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%BE%D0%BC)
5. [Результаты](https://github.com/d3enjan/sf_data_science/blob/main/PROJECT-1.%20%D0%90%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7%20%D0%B2%D0%B0%D0%BA%D0%B0%D0%BD%D1%81%D0%B8%D0%B9%20%D0%B8%D0%B7%20HeadHunter/README.md#%D1%80%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%D1%8B)
6. [Выводы](https://github.com/d3enjan/sf_data_science/blob/main/PROJECT-1.%20%D0%90%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7%20%D0%B2%D0%B0%D0%BA%D0%B0%D0%BD%D1%81%D0%B8%D0%B9%20%D0%B8%D0%B7%20HeadHunter/README.md#%D0%B2%D1%8B%D0%B2%D0%BE%D0%B4%D1%8B)


### Описание проекта
Представьте, что вы работаете датасаентистом в компании Booking. Одна из проблем компании — это нечестные отели, которые накручивают себе рейтинг. Одним из способов нахождения таких отелей является построение модели, которая предсказывает рейтинг отеля. Если предсказания модели сильно отличаются от фактического результата, то, возможно, отель играет нечестно, и его стоит проверить.


### Какой кейс мы решаем
Условия соревнования:
Данное соревнование является бессрочным и доступно для всех потоков.

Срок выполнения соревнования устанавливается индивидуально в каждом потоке.

Тестовая выборка представлена в LeaderBoard целиком.

Делаем реальный ML продукт, который потом сможет нормально работать на новых данных.

### Краткая информация о данных
Данне представлены в csv формате, cкачать нужно три файла. Файл (hotels_test)- тестовые данные, второй файл (hotels_train) данные для тренировки, и файл (submission), которые можно скачать по ссылке:

:arrow_right:[hotels](https://disk.yandex.ru/d/TEXJ7_FiGXlS6w)


### Этапы работы над проектом
1. Постановка задачи
2. Исследование структуры данных
3. Преобразование данных
4. Исследование зависимостей в данных
5. Очистка данных
6. Создание новых признаков
7. Создание и обучение модели

# Результаты
Была построена модель, показывающая существенное улучьшение MAPE: 0.12575704607627303

 # Выводы
Модель предсказывает рейтинг отеля, уверен это не предел, дальше в свободное время продолжу улучьшать модель.
 ....
 :arrow_up:[к оглавлению](https://github.com/d3enjan/sf_data_science/tree/main/PROJECT-1.%20%D0%90%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7%20%D0%B2%D0%B0%D0%BA%D0%B0%D0%BD%D1%81%D0%B8%D0%B9%20%D0%B8%D0%B7%20HeadHunter#-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82-%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7-%D0%B2%D0%B0%D0%BA%D0%B0%D0%BD%D1%81%D0%B8%D0%B9-%D0%BD%D0%B0-hhru)




