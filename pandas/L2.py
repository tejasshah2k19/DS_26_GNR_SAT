#dataframe -> add update remove ? 
#yes col row 

import pandas as pd 

data = {
    "Name":["Abhishek","Mohak","Vishwa","Khyati","Diya","Devam"],
    "Age":[25,27,26,28,30,33],
    "City":["Surat","Gandhinagar","Gandhinagar","Modasa","Gandhinagar","Himmatnagar"],
    "Salary":[25000,35000,45000,55000,65000,27000]
}


df = pd.DataFrame(data)

print(df)

#new column?
#yes 
#add bonus column for employee with bonus 5000 flat. 

df["bonus"] = 5000

print("Bonus added : ")
print(df)

#add tax column for employee - tax is 10% of salary 
df["tax"] = df["Salary"] * 0.10

print("Tax Added 10% :")
print(df) 

print("Actual Salary : ")
df["take_home"] = df["Salary"] - df["tax"]  + df["bonus"]
print(df)


#can we add fix values - manually
df["department"] = ["admin","IT","IT","admin","sales","HR"] 

print("Department : ")
print(df)

#can we add col as desired position ?
#yes - using insert function 

df.insert(3,"Country","India")
print("Country Added : ")
print(df)

##############################################################################

#update 
#increase salary by 10% or 3000 
df["Salary"] = df["Salary"] + 3000
print("Salary +3000 : ")
print(df)

#increase salary of Diya by 5% 
#increase salary of Gandhinagar employees by 5%
df.loc[  df["Name"] == 'Diya',"Salary"] = 29000 
print(df)

##############################################################################