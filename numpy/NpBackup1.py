#pip install numpy 
import numpy as np 


#how to create numpy array 
#array()

arr = np.array([1,2,3,4,5,6]) #1 argument : list 
print(arr)

print(arr.itemsize) #64bits  8byte 


# list=[21,2,4,5,33,3]
list=[1,0,1,1,1,0]
arr  = np.array(list)
print(arr)


#royal => 
#attendance -> 5 * 4 => 20 * 2 => 40 * 25 => 1000 * 50 => 50,000 * 12 => 600,000 => 6L * 1 => 6L => 4.8GB  

#1  0 

print(arr.dtype) #int => int64
print(arr.itemsize) #8 byte 
print(arr.size) #total elements 

#lets degrade -> 64bit -> 32bit -> 16bit -> 8bit 

arr = np.array( [1,0,1,0,1],dtype=np.int8 ) #1byte

print(arr.dtype)
print(arr.itemsize)


#int short int long int long  


#scaler   10 
#vector   [10,20,30,40,50]
#matrix   [ [10,20,30], [20,30,40] ]
#tensor 


#range(1,10)
 
arr = np.arange(10)
print(arr)

arr = np.arange(2,10)
print(arr)

arr = np.arange(2,30,3)
print(arr)

arr = np.arange(10,2,-1)
print(arr)




arr = np.arange(10)
print(arr)

print(arr[0]) #start:0 end:size-1

print(arr[-1])#last 
print(arr[-2])#second last 

print(arr[0:4]) #0 1 2 3 
print(arr[0:4:2])#0 2 
print(arr[::]) #0--9 
print(arr[::2])#0 2 4 6 8 
print(arr[::-1]) #reverse  #




#loop 
for i in range(0,len(arr)):
    print(arr[i])

for d in arr:
    print(d)

sum = np.sum(arr)
max = arr.max()
max = np.max(arr)

#min max avg sum sort
#mean median mod 
 


arr = np.random.random(5) #0 1 
print(arr)
print(arr.dtype)


arr = np.random.randint(100) #random int => high:100 positional argument -> single size = 1   
print(arr)


arr = np.random.randint(100,size=3)
print(arr)

arr = np.random.randint(50,100,size=3)
print(arr)

arr = np.random.randint(50,100,3)
print(arr)


arr = np.random.randint(1,20,2,dtype=np.int16)
print(arr)


arr = np.linspace(1,50,10)
print(arr)

arr  , step  = np.linspace(1,50,10,retstep=True)
print(arr,step)

#arange vs linspace 



arr = np.linspace(1,10) #generate 50 num btween 1 to 10 with equal space 
print(arr)

arr = np.linspace(1,10,3) #generate 3 num btween 1 to 10 with equal space 
print(arr)


arr,step = np.linspace(1,10,3,retstep=True) #generate 3 num btween 1 to 10 with equal space 
print(arr,step)


arr,step = np.linspace(1,10,3,retstep=True,endpoint=False) #generate 3 num btween 1 to 10 with equal space 
print(arr,step)



arr = np.zeros(10)
print(arr)

arr = np.ones(10)
print(arr)


arr = np.full(6,10)
print(arr)


arr = np.full(6,"")
print(arr)


arr = np.full(6,".")
print(arr)



arr = np.full(6,10,dtype=np.int16)
print(arr)


print("===========")
arr = np.empty(10)
print(arr)





