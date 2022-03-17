import sys
sys.path.append('C:/Users/Sasha/Documents/11-SRH Heidelberg/Big Data Programming Project/hushHush-Recruiter-Group-3/Application')
import pandas as pd
import utils

#df_stack = utils.tools.pick_df(table='Stack', id_column='UserID', name_column='UserName', email_column='UserEmail',score_column='Average')
#df_git = utils.tools.pick_df(table='Github', id_column='user_list', name_column='user_name', email_column='user_email',score_column='score')
df_kaggle = utils.tools.pick_df(table='Kaggle', id_column='TeamID', name_column='TeamName', email_column='user_email',score_column='Score')
df_kaggle.to_excel('test.xlsx')
#df_twitter = utils.tools.pick_df(table='twitter', id_column='userID', name_column='username', email_column='email',score_column='score')


# github = pd.read_excel(r"C:\Users\oates\OneDrive\Belgeler\Masters\Bigdata\github_1.xlsx")
# kaggle = pd.read_excel(r"C:\Users\oates\OneDrive\Belgeler\Masters\Bigdata\kaggle_1.xlsx")
# twitter = pd.read_excel(r"C:\Users\oates\OneDrive\Belgeler\Masters\Bigdata\twitter_1.xlsx")
# stack = pd.read_excel(r"C:\Users\oates\OneDrive\Belgeler\Masters\Bigdata\stack_1.xlsx")
# print("twitter",twitter.head())
# print("kaggle",kaggle.head())
# print("stack",stack.head())
# print("github",github.head())
#
# df1=github.merge(kaggle,left_on="email"
#                  ,right_on="email",
#                 how="outer")
# print(df1.info())
#
# print("df1",df1.head())
# df2=df1.merge(stack,left_on="email",
#               right_on="email",
#               how="outer")
# print("df2",df2.head())
# df3=df2.merge(twitter,left_on="email",
#               right_on="email",
#               how="outer")
#
# df3.to_excel("all_merged.xlsx")
#
# print(df3.head())
# print(df3)