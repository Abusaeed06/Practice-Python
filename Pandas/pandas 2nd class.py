import pandas as pd
Data={'First_name':['Robin','Shahin','Nazmul','Abir'],
      'Last_name':['Khan','Khan','Haque','Hasan'],
      'full_name':['Robin Khan','Shahin Khan','Nazmul Haque','Abir Hasan'],
      'Email':['rk@gmail.com','sk@gmail.com','nh@gmail.com','ah@gmail.com']
      }
df=pd.DataFrame(Data)
print(df)
##### Filtering Data
#we want to a email of those wose last name is khan
filtt = (df['Last_name'] == 'Khan')
print(filtt)

#Applying filter to data frame
print(df[filtt])
##or
print(df[df['Last_name']=='Khan'])
##or
#Adventage of using loc
print(df.loc[filtt])
print(df.loc[filtt, 'full_name'])

filtt= (df['Last_name'] == 'Khan')&(df['First_name'] =='Shahin')
print(df[filtt])
print(df.loc[filtt,'Email'])
Filt= (df['Last_name'] == 'Hasan')|(df['First_name'] =='Robin')
print(df[Filt])
##opposite filtering
print(df[~Filt])