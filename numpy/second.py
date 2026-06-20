import numpy as np 


#array()
#dtype  : attribute 
#dtype  : parameter 


arr = np.array([1,2,3,4,5]) #numpy array 

print(arr[0])#index 0 start size-1 end 
print(arr)
print("type arr[0] =>",type(arr[0]))
print("dtype => ",arr.dtype) #attribute 
#int64  => 64bit => 8byte 


list = [1,2,3,4,5] #python list 
print(list[0])
print(list)
x = 1 # instance ->class int
y = 1.2 #
z = 'rock' #
print(type(x))
print(type(list[0]))

print("==========================")

# arr = np.array([1,2,3,4,5]) #int_ => int64
#1 lac -> 8byte -> 8L byte -> 800MB
#1 lac -> 1byte -> 1L byte 
arr = np.array([1,2,3,4,5],dtype=np.int8) #int8 -> 1 byte  
print(arr.dtype)
print(arr.itemsize)# 1byte 


list = [1,2,3,4,5] #python list 
arr = np.array(list) 

print(arr.itemsize) #8byte  