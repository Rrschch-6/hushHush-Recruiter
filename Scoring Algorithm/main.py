import sys
sys.path.append('C:/Users/Sasha/Documents/11-SRH Heidelberg/Big Data Programming Project/hushHush-Recruiter-Group-3/Scoring Algorithm/utils')

import pandas as pd
import utils

df_stack=utils.tools.pick_top(table='Stack',id_column='UserID',name_column='UserName',email_column='UserEmail',score_column='Average',percentile=0.05)
df_git=utils.tools.pick_top(table='Github',id_column='user_list',name_column='user_name',email_column='user_email',score_column='score',percentile=0.05)
df_kaggle=utils.tools.pick_top(table='Kaggle',id_column='user_list',name_column='user_name',email_column='user_email',score_column='score',percentile=0.05)

# df_git.to_excel('Data/git.xlsx')
# df_stack.to_excel('Data/stack.xlsx')

df=utils.functions.intersection(df_stack,df_git)
df.to_excel('Data/all.xlsx')

