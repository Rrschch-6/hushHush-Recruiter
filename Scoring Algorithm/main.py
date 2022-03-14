import sys
sys.path.append('C:/Users/Sasha/Documents/11-SRH Heidelberg/Big Data Programming Project/hushHush-Recruiter-Group-3/Scoring Algorithm/utils')
import sqlite3
import pandas as pd
import utils

df_stack = utils.tools.pick_df(table='Stack', id_column='UserID', name_column='UserName', email_column='UserEmail',score_column='Average')
df_git = utils.tools.pick_df(table='Github', id_column='user_list', name_column='user_name', email_column='user_email',score_column='score')
df_git = utils.tools.pick_df(table='Kaggle', id_column='TeamID', name_column='TeamName', email_column='user_email',score_column='Score')

with utils.context_managers.connection_handler() as conn:
    temp = pd.read_csv('Data/finalTwitterData.csv')
    temp.to_sql(name='twitter',con=conn,index=False)
