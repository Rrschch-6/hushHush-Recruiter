import sys
sys.path.append('C:/Users/Sasha/Documents/11-SRH Heidelberg/Big Data Programming Project/Github-User-Data-Fetch/utils')
import pandas as pd
import utils
import context_managers
import numpy
from sklearn import preprocessing


with utils.context_managers.connection_handler() as conn:
    df=pd.read_sql_query("SELECT * FROM github_users",conn)

scaler=preprocessing.MinMaxScaler()
df[["Scaled_user_followers"]] = scaler.fit_transform(df[["user_followers"]])
df[["Scaled_user_stars"]] = scaler.fit_transform(df[["user_stars"]])
df[["Scaled_user_repos"]] = scaler.fit_transform(df[["user_repos"]])
df['score'] = df[["Scaled_user_followers","Scaled_user_stars","Scaled_user_repos"]].mean(axis=1)

df.to_excel('Output Files/Github_Data_with Score_6_March.xlsx',index=False)

