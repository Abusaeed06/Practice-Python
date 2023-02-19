#import pandas library
import pandas as pd
# 1.Creating a dictonary of some keys(_) and values(_)
Data={'First':['Robin','Shahin','Nazmul','Abir'],
      'Last':['Khan','Khan','Haque','Hasan'],
      'Email':['rk@gmail.com','sk@gmail.com','nh@gmail.com','ah@gmail.com']
      }
df=pd.DataFrame(Data)
print(df)

#2.Accessing Column
#There are two methods to access a columns
#Using square bracket[]

print(df['First'])
print(type(df['First']))
#Using (.) notation
print(df.Email)
# 3.Accessing more than one column
print(df[['First','Last']])
print(type(df[['First','Last']]))

# 4. Accessing the Column name together
print(df.columns)

### accessing Rows
##.loc() method
##.iloc() method
#iloc allows to access value using integer location.
# iloc (inntneger location)
print(df)
print(df.iloc[0]) # will give us all the data of first row
print(df.iloc[[0,2,3]]) # will give us specific rows
# To access an individual value we need to pass the integer location of the value
#df.iloc[rows,columns]
print(df.iloc[3,2])
##.loc method
#using .loc() method we will be able to access value by passing column name
# we wnat to access the first name of the first row
print(df.loc[2,'First'])
# accessing multiple row's values using .lock() method
print(df.loc[[0,1,2],'Email'])#particular value
print(df['Email'])#all value
print(df.loc[[0,2,3],['Email','Last']]) #getting specific columns of rows
##detecting index
A=list(df.columns)
print(A)
print(A.index('Email'))
##Adding column
full_name=df['First']+' '+df['Last']
print(full_name)
####5.Adding column to the end
df['Full_name']=full_name
print(df)
###6. Adding column to a specific position

df.insert(2,'Full_Name','Full_name')
print(df)
##Drop column
df.drop('Full_name',axis=1,inplace=True)
print(df)
###Column Rename
df.rename(columns={
      'First':'First_Name',
      'Last':'Last_Name'
},inplace=True)
print(df)

