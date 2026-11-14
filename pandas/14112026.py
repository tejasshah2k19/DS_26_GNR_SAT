import pandas as pd 
# marks = pd.Series([80,70,90,60,95],index=["Maths","Eng","Sci","Hindi","Computer"])
marks = pd.Series([80,70,90,60,95])

# print(marks)

# print(marks.min())
print(marks.idxmin())
print(marks.count()) #5

#marks.mean() sum() max() min() median() count()


marks = pd.Series([80,None,90,60,95],index=["Maths","Eng","Sci","Hindi","Computer"])
print(marks.count()) # 4 

#idxmin()
#idxmax()

#describe() 

#frequency count? 



marks = pd.Series([80,60,80,60,95])

print(marks.value_counts()) # item wise count 
print(marks.nunique()) #count total unique values 
#print all the unique marks 
print(marks.unique())