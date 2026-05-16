# # # Core Array Setup
# # import numpy as np

# # arr=np.array([1,2,3,4,5])
# # print(arr)

# # # Vectorized Operations
# # print(arr+5)
# # print(arr*2)
# # print(arr**2)


# # #2D array(Matrices)

# # matrix=np.array([
# #     [1,2,3],
# #     [4,5,6]
    
# # ])

# # print(matrix)

# # #Accessing elements in 2D array
# # print(matrix[0][1])

# # #Shape (very important in AI)
# # print(matrix.shape)

# # # Task1  Basic Array Operations

# import numpy as np
# # arr=np.array([10,20,30,40,50])
# # print(arr+5)
# # print(arr*2)
# # print(arr/2)

# ## Task 2  Statistics with NumPy
# arr=np.array([5,10,15,20])

# np.mean(arr)
# np.max(arr)
# np.min(arr)
# print(np.sum(arr))

# Matrix practice

import numpy as np
# matrix=np.array([
#                [2,4],
#                [6,8]
    
# ])

# print(matrix.shape)
# print(matrix[1][1])


# Task 4 Real AI Business Logic

prices=np.array([100,200,300,400])

#Apply 10% discount
discounted=prices*0.9
print(discounted)

# Vectorized operations (FAST computation)
# Broadcasting concept
# Matrix structure (2D data)
# Shape awareness (critical for ML models)