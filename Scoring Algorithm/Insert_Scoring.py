import sqlite3
import pandas as pd
import csv
conn = sqlite3.connect('HushHush.db')
c = conn.cursor()
print("Successfully Connected to SQLite")

v = 'stack'
select = 'select UserID,UserName,UserEmail from {} order by average desc'.format(v)
# print(select)

df = pd.read_sql(select,conn)
df['Position'] = 'TESTING'
# print(df)
df_org=df

print(len(df.index))

TOP5 = int(round(len(df.index)*0.05,0))

df_head5 = df.head(TOP5)
print('we have filtered top 5 s,develoeprs')




df_head10 = df.merge(df_head5,on=['UserID'])
#print(df_head10)
df[(~df.UserID.isin(df_head10.UserID))&(~df.UserID.isin(df_head10.UserID))]


df_head10.rename(columns={"UserName_x": "UserName", "UserEmail_x": "UserEmail"}, inplace=True)
df_head10 = df[['UserID','UserName','UserEmail']]



TOP10 = (int(round(len(df_head10.index)*0.10,0)))
df=df_head10
df_head10 = df_head10.head(TOP10)
print('we have filtered top 10 s,develoeprs')


df_head20 = df.merge(df_head10,on=['UserID'])
df[(~df.UserID.isin(df_head20.UserID))&(~df.UserID.isin(df_head20.UserID))]




df_head20.rename(columns={"UserName_x": "UserName", "UserEmail_x": "UserEmail"}, inplace=True)
df_head20 = df[['UserID','UserName','UserEmail']]

TOP20 = (int(round(len(df_head20.index)*0.20,0)))
df_head20 = df_head10.head(TOP20)

print('we have filtered top 20 s,develoeprs')


df_head20['Position'] = 'Developer'
df_head5['Position'] = 'Senior Architect'
df_head10['Position'] = 'Senior Developer'


df_union = pd.concat([df_head5,df_head10,df_head20],axis=0)


print(df_union)




