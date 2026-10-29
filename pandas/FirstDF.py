import pandas as pd 


data = {
    "name":["ram","shyam","ganshyam","sita"],
    "department":["hr","admin","sales","admin"],
    "age":[22,33,25,34],
    "salary":[15000,25000,16000,18000],
    "city":["Ahmedabad","surat","surat","Ahmedabad"]   
}

df = pd.DataFrame(data)

# print(df)

#inspect 

# print(df.head())
# print(df.tail())

# print(df.head(2)) #first 2 
# print(df.tail(2)) #last 2 


# print(df.sample(2)) #random any 2 

# print(df.shape)
# print(df.columns)
# print(df.index)
#data types of each col 
# print(df.dtypes)

#summary 
# print(df.info())
# print(df.describe())

#memory 
# print(df.memory_usage())



#tabular data -> access --> rows -- columns 

#column 

#print all employee name 
# print(df["name"]) #pluck column -> name  -> it reutrn column -> name -> as series 
# print(type(df["name"]))
#extact single column 'name' as data frame 

# print(df[["name"]])
# print(type(df[["name"]]))

#extract name and salary 
# print(df[["name","salary"]])


#extract row 
# print(df.loc[0])  #0 => label 

# print(df.loc[0:2]) #0 1 2 


# #row and col 
# print(df.loc[2,"name"])

# print(df.loc[2,["name","salary"]])



#pure --> integer position 


# print(df.iloc[0])  #0 => 0th row  

# print(df.iloc[0:2]) #0 1 2 


# #row and col 
# print(df.iloc[2,0])
# print(df.iloc[2,0:2])



"""
                    loc             iloc
selection           labels          integer positions 
slice end index     included        excluded 
slice index e.g     0:2 => 0 1 2    0:2 => 0 1 
name col            yes             no 
name col e.g        loc["name"]     iloc[0]
"""

#custom lable for data frame 

data = {
    "name":["ram","shyam","ganshyam","sita"],
    "salary":[15000,25000,16000,18000],
}

df1 = pd.DataFrame(data) #lable => index 0 1 2 3 
df2 = pd.DataFrame(data,index=["R101","R102","R103","R104"])

# print(df1)
# print("*"*10)
# print(df2)



# print(df1.loc[0])
# print(df2.loc["R101"])
print("*"*20)
print(df2.loc["R101","name"])
print("*"*20)
print(df2.loc["R101":"R103","name"])
print("*"*20)