import sys
sys.path.append('C:/Users/Sasha/Documents/11-SRH Heidelberg/Big Data Programming Project/hushHush-Recruiter-Group-3/Scoring Algorithm/utils')
import pandas as pd

def step_1(p1,p2,p3):

    df_stack=utils.tools.pick_df(table='Stack',id_column='UserID',name_column='UserName',email_column='UserEmail',score_column='Average')
    df_git=utils.tools.pick_df(table='Github',id_column='user_list',name_column='user_name',email_column='user_email',score_column='score')
    df_kaggle=utils.tools.pick_df(table='Kaggle',id_column='user_list',name_column='user_name',email_column='user_email',score_column='score')

    df_stack_p1=utils.tools.pick_top(dfdf_stack,percentile=p1)
    df_git_p1 = utils.tools.pick_top(df=df_git, percentile=p1)
    df_kaggle_p1 = utils.tools.pick_top(df=df_git, percentile=p1)

    df_architect=pd.concat([df_stack_p1,df_git_p1,df_kaggle_p1]).drop_duplicates(subset=['email'])

    df_stack_p2=utils.tools.pick_top(utils.tools.difference(df_stack_p1,df_stack),percentile=p2)
    df_git_p2 = utils.tools.pick_top(utils.tools.difference(df_stack_p1, df_stack), percentile=p2)
    df_kaggle_p2 = utils.tools.pick_top(utils.tools.difference(df_stack_p1, df_stack), percentile=p2)

    df_senior = pd.concat([df_stack_p2, df_git_p2, df_kaggle_p2]).drop_duplicates(subset=['email'])

    df_stack_p3 = utils.tools.pick_top(utils.tools.difference(df_stack_p2, df_stack), percentile=p3)
    df_git_p3 = utils.tools.pick_top(utils.tools.difference(df_stack_p2, df_stack), percentile=p3)
    df_kaggle_p3 = utils.tools.pick_top(utils.tools.difference(df_stack_p2, df_stack), percentile=p3)

    df_developer = pd.concat([df_stack_p3, df_git_p3, df_kaggle_p3]).drop_duplicates(subset=['email'])

    return pd.concat([df_architect,df_senior,df_developer])
