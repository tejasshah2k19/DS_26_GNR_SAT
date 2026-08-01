import pandas as pd


maths = [90,92,45,67]

s1  = pd.Series(maths)

print(s1)

employee =  {  
                "name":["rock","sakira","jack"],
                "salary":[25000,45000,35000]
           }

df = pd.DataFrame(employee)


print(df)
print(df["name"])


print("******")
print(df.iloc(0))
print("******")
print(df.loc[0,"name"])
print("******")
print(df.iloc[0])

print("******")
print(df.iloc[0:2])


#iloc -> integer location 
#iloc[X,Y]  x => row y => col 
#iloc[X]

print("******")
print(df.iloc[0,0])
print(df.iloc[0,1]) #name : rock salary: 25000


print("******all salary*****")
print(df.iloc[::,1])

print("******all empname*****")
print(df.iloc[::,0])
