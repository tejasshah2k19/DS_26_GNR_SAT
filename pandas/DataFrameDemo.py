import pandas as pd 


data ={ 
       "name" : ["a","b"],
        "age" : [25,30],
        "salary" : [18000,2000]
}


df = pd.DataFrame(data)

# fileData = pd.read_csv("users_50.csv")


print(df)

cities = ['surat','baroda']

df['city'] = cities 

print(df)



users = [
    {
        "name":"ram",
        "salary":15000,
        "age":25
    },
    {
        "name":"ravan",
        "salary":16000,
        "age":26
    }
]

df = pd.DataFrame(users)

print(df)


users = { 
    {
        "name":"ram",
        "salary":15000,
        "age":25
    },
    {
        "name":"ravan",
        "salary":16000,
        "age":26
    }
}


#5000 records 
#top five records fetch 
df.head(5)
df.tail(5)

df.columns 
df.shape
df.dtypes

df.info() 
df.describe()






