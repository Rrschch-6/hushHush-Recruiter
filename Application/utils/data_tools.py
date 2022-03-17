import sys
sys.path.append('C:/Users/Sasha/Documents/11-SRH Heidelberg/Big Data Programming Project/hushHush-Recruiter-Group-3/Application')
import pandas as pd
import utils

def creat_HushHush():


def merge():
    df_stack = utils.tools.pick_df(table='Stack', id_column='UserID', name_column='UserName', email_column='UserEmail',score_column='Average')
    df_github = utils.tools.pick_df(table='Github', id_column='user_list', name_column='user_name', email_column='user_email',score_column='score')
    df_kaggle = utils.tools.pick_df(table='Kaggle', id_column='TeamID', name_column='TeamName', email_column='user_email',score_column='Score_normalised')
    df_twitter = utils.tools.pick_df(table='twitter', id_column='userID', name_column='username', email_column='email',score_column='score')

    df1=df_github.merge(df_kaggle,left_on="email",right_on="email",how="outer")
    df1=df1.drop(columns=['id','user_name_x','TeamId','user_name_y'])
    df2=df1.merge(df_stack,left_on="email",right_on="email",how="outer")
    df2=df2.drop(columns=['id','user_name'])
    df3=df2.merge(df_twitter,left_on="email",right_on="email",how="outer")
    df=df3.drop(columns=['id','user_name'])
    return df
