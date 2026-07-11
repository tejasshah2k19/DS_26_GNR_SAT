import numpy as np 

a = [1,2,3,4,5]

b = [ [1,2,3],[4,5,6],[7,8,9] ]


arr = np.array([1,2,3,4,5])
print(arr.ndim)#1 
print(arr.size)#5 
print(arr.itemsize)
print(arr.size * arr.itemsize)
print(len(arr))
print("===========================")
arr = np.array([ [1,2,3],[4,5,6],[7,8,9] ])
print(arr.ndim)#2
print(arr.size)#9 
print(arr.itemsize)

# arr = np.array(b) 
# 


print("===========================")
arr = np.array([ [1,2,3],[4,5,6],[7,8,9] ])
print(arr.dtype)#int64 => 8 byte 


arr = np.array([ [1,2,3],[4,5,6],[7,8,9] ],dtype=np.int16)
print(arr.dtype)#int16 => 2 byte 


arr = np.arange(10)
print(arr)


arr = np.arange(5,10)
print(arr)


arr = np.random.random(5)
print(arr)

arr = np.random.randint(1,100,10)
print(arr)


arr = np.zeros(10,dtype=int)
print(arr)

arr = np.ones(10,dtype=int)
print(arr)


arr = np.zeros((2,3),dtype=int)
print(arr)

arr = np.ones((4,3),dtype=int)
print(arr)


arr = np.linspace(1,10)
print(arr)