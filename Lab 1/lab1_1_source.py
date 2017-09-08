"""
1. Заменить минимальный элемент побочной диагонали на среднюю сумму
отрицательных элементов матрицы P[n,n].
"""

import numpy as np

np.set_printoptions(precision=2)

arr = np.random.randint(-30, 30, (5, 5))
diag = np.diag(np.fliplr(arr))
min_elem_index = diag.argmin()
avrg_sum = arr[arr < 0].mean()
min_elem_row, min_elem_columns = min_elem_index, arr.shape[1] - min_elem_index - 1

print('Default array:')
print(arr)
print('Index of minimal: {0}x{1}'.format(min_elem_row, min_elem_columns))
print('Negative numbers:', arr[arr < 0])
print('Average negative value: ', avrg_sum)
arr = arr.astype(float)
arr[min_elem_row, min_elem_columns] = avrg_sum
print('Result array:')
print(arr)