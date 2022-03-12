import sys
sys.path.append('C:/Users/Sasha/Documents/11-SRH Heidelberg/Big Data Programming Project/hushHush-Recruiter-Group-3/Data Source Github/utils')
import pandas as pd
import utils
import context_managers
import numpy
from sklearn import preprocessing
import sqlite3

conn = sqlite3.connect('Output Files/github_database.db')
c = conn.cursor()
c.execute('DROP TABLE github_users')
df=pd.read_excel('Output Files/Github Data_March_6.xlsx')
df.to_sql(name='github_users',con=conn)
conn.commit()
conn.close()
# with utils.context_managers.connection_handler() as conn:
#     df=pd.read_sql_query("SELECT * FROM github_users",conn)
#
# with utils.context_managers.cursor_handler() as c:
#     c.execute('SELECT * FROM github_users',c)
#     c.fetchall()
#
# print(df.head())
# scaler=preprocessing.MinMaxScaler()
# df[["Scaled_user_followers"]] = scaler.fit_transform(df[["user_followers"]])
# df[["Scaled_user_stars"]] = scaler.fit_transform(df[["user_stars"]])
# df[["Scaled_user_repos"]] = scaler.fit_transform(df[["user_repos"]])
# df['score'] = df[["Scaled_user_followers","Scaled_user_stars","Scaled_user_repos"]].mean(axis=1)
#
# df.to_excel('Output Files/Github_Data_with Score_6_March.xlsx',index=False)
#
