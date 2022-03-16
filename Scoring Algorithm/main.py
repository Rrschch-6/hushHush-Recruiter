import sys
sys.path.append('C:/Users/Sasha/Documents/11-SRH Heidelberg/Big Data Programming Project/hushHush-Recruiter-Group-3/Scoring Algorithm/utils')
import sqlite3
import pandas as pd
import utils

df_stack = utils.tools.pick_df(table='Stack', id_column='UserID', name_column='UserName', email_column='UserEmail',score_column='Average')
df_git = utils.tools.pick_df(table='Github', id_column='user_list', name_column='user_name', email_column='user_email',score_column='score')
df_kaggle = utils.tools.pick_df(table='Kaggle', id_column='TeamID', name_column='TeamName', email_column='user_email',score_column='Score')
df_twitter = utils.tools.pick_df(table='twitter', id_column='userID', name_column='username', email_column='email',score_column='score')



df=utils.tools.datasource_merge(df_kaggle,df_git,df_stack,df_twitter)
df.to_excel('Da


