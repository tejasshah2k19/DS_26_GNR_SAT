import numpy as np 

arr , st  = np.linspace(1,10,5,retstep=True)
print(arr)
print(st)


arr = np.linspace(1,50,20).reshape((4,5))

print(arr)
print(arr.shape)

print(np.linspace(10,10,2))

print(np.linspace(1 ,100,5,endpoint=False))
 

arr = np.empty(10)
# arr = np.arange(1,11)

for i  in range(0,10):
    arr[i] = i+1;

print(arr)




arr = np.empty(10)
arr[:] = np.arange(1,11)
