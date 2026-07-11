import numpy as np 

arr = np.array([ [1,2,3],[4,5,6],[7,8,9]  ])

print(arr)

print(arr[0])
print(arr[-1])
print(arr[0,2])


print("==============")
print(arr[0,:]) 
print(arr[0,0:2])#0th row 0:2 {0:inc 2:exc}



print("==============")
print(arr[:,1])
print(arr[0:2,1])


#print two rows 
print(arr[0:2])







