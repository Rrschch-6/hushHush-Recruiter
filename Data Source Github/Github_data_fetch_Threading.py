import sys
sys.path.append('C:/Users/Sasha/Documents/11-SRH Heidelberg/Big Data Programming Project/Github-User-Data-Fetch/utils')
from github import Github
import pandas as pd
import time
import datetime
from threading import Thread
import utils

with utils.context_managers.cursor_handler() as c:
    utils.tools.create_table('github_users',c)

github_token=''
g=Github(github_token)
user_name = []
user_followers = []
user_created_at = []
user_twitter_username = []
user_stars = []
user_repos = []
user_languages = []
user_emails = []

def fetch_user(number_of_users):
    print(f'Please wait while listing {number_of_users} users, in order that they signed up in Github')
    github_user_list=[]

    for i in range(number_of_users):
        try:
            github_user_list.append(g.get_users()[i].__str__().split('"')[1])
            print('\r',i,g.get_users()[i].__str__().split('"')[1],end=" ")
        except:
            if g.rate_limiting[0] == 0:
                time_delay = int((datetime.datetime.fromtimestamp(g.rate_limiting_resettime) - datetime.datetime.now()).total_seconds() + 15)
                mins, secs = divmod(time_delay, 60)
                print(f'Error occurred during listing users,Github rate exceeded,please wait {mins}:{secs}')
                utils.tools.countdown(time_delay)
                continue
            else:
                time_delay=10
                mins, secs = divmod(time_delay, 60)
                print(f'Error occurred during listing users,Github rate exceeded,please wait {mins}:{secs}')
                utils.tools.countdown(time_delay)
                continue

    print('\r',f'{number_of_users} Github User_Name listed',end=" ")
    return github_user_list

def fetch_data(*args):


    for i in range(len(args)):
        try:
            user=g.get_user(args[i])
            user_name.append(user.name)
            user_followers.append(user.followers)
            user_created_at.append(user.created_at)
            user_twitter_username.append(user.twitter_username)
            user_stars.append(user.get_starred().totalCount)
            user_repos.append(user.get_repos().totalCount)
            print(i,user.get_repos()[0])
            #user_languages.append(g.get_repo(user.get_repos()[0].__str__().split('"')[1]).language)
            user_emails.append(user.email)
            print('\r',i,args[i])


        except:
            if g.rate_limiting[0] == 0:
                time_delay = int((datetime.datetime.fromtimestamp(g.rate_limiting_resettime) - datetime.datetime.now()).total_seconds() + 15)
                utils.tools.countdown(time_delay)
                continue
            else:
                time_delay = 10
                time.sleep(time_delay)
                continue


    print(f'data fetched')


#using threads for executing functions

n=20000
github_user_list=fetch_user(n)
github_user_list=df_users['user_list'].to_list()
github_user_list=github_user_list[0:30]
chunks = utils.tools.splitList(github_user_list, 5)
threadlist=[]

for i in range(len(chunks)):
    t = Thread(target=(fetch_data), args=(chunks[i]))
    threadlist.append(t)
    t.start()


for j in threadlist:
    j.join()

print(len(user_name),user_languages)
with utils.context_managers.cursor_handler() as c:
    for i in range(len(github_user_list)):
        print(i,user_languages[i])
       # utils.tools.insert_user('github_users', github_user_list[i], user_name[i], user_followers[i], user_created_at[i],user_twitter_username[i], user_stars[i], user_repos[i],user_languages[i],user_emails[i], c)

#creating pandas dataframe from sqlite3 table
with utils.context_managers.connection_handler() as conn:
    df=pd.read_sql_query("SELECT * FROM github_users",conn)
    print(df.head)

#exporting excel file from pandas dataframe
df.to_excel('Output Files/database_to_excel.xlsx',sheet_name='main',index=False)

with utils.context_managers.cursor_handler() as c:
    print(utils.tools.table_count('github_users',c))


