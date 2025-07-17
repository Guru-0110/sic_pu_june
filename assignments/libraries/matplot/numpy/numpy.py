import numpy as np
from scipy import stats
# list1 = np.array([[1,2,3,4,5,6,7], [8,9,10,11,12,13,14]])

# mode_value = stats(list1)
# print(mode_value)

array1=np.zeros(3)
array2=np.zeros((2,4))
array3=np.zeros((3,12))
print(array1)
print(array2)
print(array3)


array4=np.full((2,4),5,dtype =int)
print(array4)

array5=np.arange(1,10)
array6=np.arange(10,20)
print(array6)

array7=np.ones(10)
array8=np.ones((1,3))
array9=np.ones((2,4))
array10=np.ones((3,4))
print(array7)
print(array8)
print(array9)
print(array10)

vector=np.arange(5)
print(vector.shape)

matrix =np.ones((2,3))
print(matrix)
print(matrix.shape)

tensor =np.zeros([2,3,3])
print(tensor.shape)


#reshape for reshaping the original matrix


array11 = np.arange(1,10).reshape(3,-1)
print(array11)
