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


