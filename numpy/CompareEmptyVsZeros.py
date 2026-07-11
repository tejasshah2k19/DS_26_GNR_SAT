import numpy as np 
import time 


start=time.time() 
arr = np.zeros(10000)
end=time.time() 
zero = end-start


start=time.time() 
arr = np.empty(10000)
end=time.time() 
empty = end-start 

print(zero-empty) #neg 
print(empty-zero) #pos 


