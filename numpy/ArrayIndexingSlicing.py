import numpy as np 


arr = np.array([10,20,30,40,50])

#index 
#start : 0
#ends  : SIZE - 1 


print(arr.size)
print(arr[0]) # 10 
print(arr[arr.size-1]) # 50 

#negative indexing 
print(arr[-1]) # minus end access rightside -> -1 -2 -3
print(arr[-2]) # 

#slicing 
print(arr[0:3]) # 0 1 2 
print(arr[0:5:1]) #0 1 2 3 4 
print(arr[0:5:2]) #0 2 4 

print(arr[0:5:-1])  

print(arr[4:0:-1])  

print(arr[::]) 
print(arr[::-1]) 



print("===============")
arr = np.random.randint(1,50,10) 
print(arr)

ans = arr > 25
print(ans)
print(arr[ans])
print(arr[arr>25])