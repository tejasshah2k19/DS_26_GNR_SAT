#numpy 
#single data type

#matrix -> highest data type 

#marks perc --> float 

#name marks perc --> string 
#pandas --> Series 
#pandas -> DataFrame 

#pip install pandas 
 
import pandas as pd 


# pd.Series([])

data = {
    "Name":["Ram","Shyam","Ganshyam","RadheShyam","Ravan"],
    "Maths":[85,90,80,95,60],
    "Sci":[90,95,80,95,90],
    "Eng":[80,85,90,95,90],
    "City":["LA","NY","SD","NY","LA"]
}

df = pd.DataFrame(data)


print(df)


print("Head => 3")
print(df.head(3))

print("Tail => 3")
print(df.tail(3))

print(df.dtypes)

#unicode -> <U10  --> object 


print(df.shape)
print(df.ndim)
print(df.size)

#we want to access particular item(s)
#row
#iloc() --> integer location {starts with zero} 

print(df.iloc(0)) #function --- address --- object 
print(df.iloc[0]) #value
print(df.iloc[0:2])#0 1  second argument exclusive 



#can we access particular col? 
#print all students name 
print(df.iloc[::,0])


#loc() 
print(df)

df = pd.DataFrame(data,index=["s1","s2","s3","s4","s5"])
print(df)

print(df.iloc[0])# ? 
print(df.loc["s1"])




df = pd.DataFrame(data)

#conditional --- filtering 


maths = df["Maths"] >= 85 

print(maths)

maths85  = df[maths] 

print("Maths 85 ")
print(maths85)
"""
0   True 
1   True 
2   False
3   True
4   False
"""


print("****************************")
maths85 = df[  df["Maths"]>=85   ]
print(maths85)


#multiple condition => maths >=85 and sci>=90 
#AND && & 

print("Maths85Sci90")
maths85Sci90 = df [   (df["Maths"]>=85) & (df["Sci"]>=95)   ]
print(maths85Sci90)


#OR -> | 

print(df[ df["City"] == "LA"] )
print(df[ df["City"] == "LA"] )


#LA NY SD PT 
print(df[  df["City"].isin(["LA","NY","PT","SD"]) ])
#not isin 
print(df[  ~df["City"].isin(["SD"]) ])


#string 
#list all students who's name starts with S
#list all students who's name contains S

print("Name that contains => S")
print( df[   (df["Name"].str.contains("s"))  | (df["Name"].str.contains("S"))])


print("Ends with M ")
print(df[  df["Name"].str.endswith("m")  ])


#maths > 85 and city = LA students ? 
print("Maths > 85 & city = LA ")
print(df[   (df["Maths"] >= 85 ) & (df["City"] == "LA")  ])

#query() 
print( df.query("Maths >= 85 and City == 'LA' ") )
 