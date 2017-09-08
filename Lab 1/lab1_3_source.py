"""
3. Из положительных элементов массива Х1, Х2 , ... , Хn, расположенных правее
минимального элемента, сформировать новый массив.
"""

import numpy as np

X = np.random.randint(-50, 50, 25)
print(X)
min_index = X.argmin()
print('Index of minimal value: {0}, minimal value: {1}'.format(min_index, X[min_index]))
result = X[min_index+1:]
result = result[result > 0]
print('All positives after {0}: {1}'.format(X[min_index], result))