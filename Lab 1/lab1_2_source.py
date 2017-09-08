"""
2. В матрицах A[m,n], B[m,n] найти и поменять местами максимальный элемент
среди нечётных столбцов и чётных строк соответственно
"""

import numpy as np

A = np.random.randint(0, 50, (3, 5))
B = np.random.randint(0, 50, (3, 5))
print(A)
print(B)

A_temp = np.array(A)
A_temp[:, ::2] = np.iinfo(A_temp.dtype).min # обращаем четные столбцы в минимально возможное числа

B_temp = np.array(B)
B_temp[1::2, :] = np.iinfo(A_temp.dtype).min # обращаем  нечетные строки в минимально возможно числа

A_max_ind = np.unravel_index(A_temp.argmax(), A_temp.shape)
B_max_ind = np.unravel_index(B_temp.argmax(), B_temp.shape)

print('\nSwapping {0} in {1} and {2} in {3}...\n'.format(A[A_max_ind], A_max_ind, B[B_max_ind], B_max_ind))

A[A_max_ind], B[B_max_ind] = B[B_max_ind], A[A_max_ind]
print(A)
print(B)