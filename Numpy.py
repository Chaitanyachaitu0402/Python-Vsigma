# Converting the Lists to arrays by using Numpy

import numpy as np

x = np.array([1,2,3,4,5])
print(x)
print(type(x))
print(x.ndim)

y=[1,2,3,4]
print(y)
print(type(y))

# Creating the Numpy Array

l = []
for i in range(1,5):
    int_1 = int(input("enter : "))
    l.append(int_1)
print(np.array(l))

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

# How to create Numpy Array using Numpy Function / Special Numpy Array

# Zeros

zero = np.zeros(4)
zero1 = np.zeros((3,4))

print(zero)
print()
print(zero1)

# Ones

one = np.ones(4)
one1 = np.ones((3,4))

print(one)
print()
print(one1)

# Empty

empty = np.empty(4)

print(empty)

# Range

range = np.arange(4)

print(range)

# Diagonal

dia = np.eye(4,5)
print(dia)

# LineSpace

lin = np.linspace(0,20,num=5)

print(lin)

# Numpy random arrays

# rand()

var = np.random.rand(4,7)

print(var)

# randn()
var1 = np.random.randn(5)
print(var1)

# ranf()

var2 = np.random.ranf(4)
print(var2)

# randint()

var3 = np.random.randint(4,20,5)
print(var3)

# Data Types

var = np.array([1,2,3,4])
print("Datatype: ",var.dtype)

var = np.array([1.0,2.0,3.4,4.6])
print("Datatype: ",var.dtype)

var = np.array(["a","b","c","d"])
print("Datatype: ",var.dtype)

var = np.array([1,2,3,4],dtype = np.int8)
print("Datatype: ",var.dtype)

var = np.array([1,2,3,4],dtype = "f")
print("Datatype: ",var.dtype)
print(var)

var = np.array([1,2,3,4])
new = np.float32(var)
print("Datatype: ",var.dtype)
print("Datatype: ",new.dtype)
print(var)
print(new)

var = np.array([1,2,3,4])
new = var.astype(float)
print(var)
print(new)

# Arthmetic Operations in Numpy

# Addtion

x = np.array([1,2,3,4])
y = np.array([1,2,3,4])

result = x + y

print("Result: ",result)

# Substraction

x = np.array([1,2,3,4])
y = np.array([1,2,3,4])

result = x - y

print("Result: ",result)

# Division

x = np.array([1,2,3,4])
y = np.array([1,2,3,4])

result = x / y

print("Result: ",result)

# Module Divsion

x = np.array([1,2,3,4])
y = np.array([1,2,3,4])

result = x % y

print("Result: ",result)

# Reciprocal

x = np.array([1,2,3,4])

varadd = np.reciprocal(x)

print(varadd)

# Two Dimensional Arthmetic in Numpy Arrays

x = np.array([[1,2,3,4],[1,2,3,4]])
y = np.array([[1,2,3,4],[1,2,3,4]])

result = x + y
print("Result: ",result)

# Arithmetic Functions

# np.min(x)

var = np.array([1,2,3,4])

print(np.min(var))
print(np.max(var))
print(np.argmin(var))
print(np.sqrt(var))
print(np.sin(var))
print(np.cos(var))
print(np.cumsum(var))

# Shape and Reshape of the Array

var = np.array([[1,2,3,4],[1,2,3,4]])

print(var)
print()
print(var.shape)

var = np.array([1,2,3,4],ndmin=4)

print(var)
print(var.ndim)
print()
print(var.shape)

var = np.array([1,2,3,4,5,6])
print(var)

print()

x = var.reshape(3,2)
print(x)

# Indexing and Slicing

# Indexing

var = np.array([1, 2, 3, 4])

print(var[1])
print(var[-1])


var = np.array([[1,2,3,4],[1,2,3,4]])
print(var[0,1])

var = np.array([[[1,2,3,4],[1,2,3,4],[1,2,3,4]]])
print(var[0,0,1])

# slicing

var = np.array([1,2,3,4])
print(var[1:])
print(var[1:3])