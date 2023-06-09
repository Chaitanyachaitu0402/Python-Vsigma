# Converting the Lists to arrays by using Numpy

import numpy as np

# x = np.array([1,2,3,4,5])
# print(x)
# print(type(x))
# print(x.ndim)

# y=[1,2,3,4]
# print(y)
# print(type(y))

# # Creating the Numpy Array

# l = []
# for i in range(1,5):
#     int_1 = int(input("enter : "))
#     l.append(int_1)
# print(np.array(l))  

# Types of the arrays

# One Dimensional Array

x = np.array([1,2,3,4])
print(x)
print(x.ndim)

# Two Dimensional Array

x = np.array([[1,2,3,4],[1,2,3,4]])
print(x)
print(x.ndim)

# Three Dimesional Array

x = np.array([[[1,2,3,4],[1,2,3,4],[1,2,3,4]]])
print(x)
print(x.ndim)

# ndimesional Array

x = np.array([1,2,3,4], ndmin = 10 )
print(x)
print(x.ndim)