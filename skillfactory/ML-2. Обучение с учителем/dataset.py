import pandas as pd 
import numpy as np
from sklearn import linear_model
from sklearn.datasets import load_boston 
from sklearn import metrics

import matplotlib.pyplot as plt #для визуализации
import seaborn as sns #для визуализации
# %matplotlib inline
plt.style.use('seaborn') #установка стиля matplotlib
from sklearn.datasets import load_boston 

boston = load_boston()
#создаём DataFrame из загруженных numpy-матриц
boston_data = pd.DataFrame(
    data=boston.data, #данные
    columns=boston.feature_names #наименования столбцов
)
#добавляем в таблицу столбец с целевой переменной
boston_data['MEDV'] = boston.target
 
#Составляем список факторов (исключили целевой столбец)
features = boston_data.drop('MEDV', axis=1).columns
#Составляем матрицу наблюдений X и вектор ответов y
X = boston_data[features]
y = boston_data['MEDV']




print('Все работает?')    
