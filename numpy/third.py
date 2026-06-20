import numpy as np 


arr = np.array([1,2,3,4,5]) #numpy array


#index 
#0 to size -1 
#can we have negative index ?
print(arr[-1]) 

#do we haave slicing ? 
print(arr[0:3]) #0 1 2 
 
print(arr[::]) # full print  
print(arr[::1]) # full print  
print(arr[::2]) # full print  1 3 5 
print(arr[::-1]) # reverse 


