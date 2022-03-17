import sys
sys.path.append('C:/Users/Sasha/Documents/11-SRH Heidelberg/Big Data Programming Project/hushHush-Recruiter-Group-3/Data Source Github/utils')
from github import Github
import pandas as pd
import time
import datetime
from threading import Thread
import utils

with utils.context_managers.cursor_handler() as c:
  utils.tools.create_table('github_users',c)

github_token='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'
g=Github(github_token)

def fetch_user(number_of_users):

  print(f'Please wait while listing {number_of_users} users, in order that they signed up in Github')
  github_user_list = []

  for i in range(number_of_users):

    try:
      github_user_list.append(g.get_users()[i].__str__().split('"')[1])
      print('\r', i, g.get_users()[i].__str__().split('"')[1], end=" ")

    except:
      if g.rate_limiting[0] == 0:
        time_delay = int((datetime.datetime.fromtimestamp(g.rate_limiting_resettime) - datetime.datetime.now()).total_seconds() + 15)
        mins, secs = divmod(time_delay, 60)
        print(f'Error occurred during listing users,Github rate exceeded,please wait {mins}:{secs}')
        utils.tools.countdown(time_delay)
        continue

      else:
        time_delay = 10
        mins, secs = divmod(time_delay, 60)
        print(f'Error occurred during listing users,Github rate exceeded,please wait {mins}:{secs}')
        utils.tools.countdown(time_delay)
        continue
  print('\r', f'{number_of_users} Github User_Name listed', end=" ")
  return github_user_list


def fetch_data(user_list):

  counter=0
  with utils.context_managers.cursor_handler() as c:
    for i in range(len(user_list)):
      print(i,user_list[i])

      try:
        user=g.get_user(user_list[i])
        if user.get_repos().totalCount == 0:
          user_language=""
        else:
          user_language=g.get_repo(user.get_repos()[0].__str__().split('"')[1]).language

        utils.tools.insert_user('github_users',user_list[i],user.name,user.followers,user.created_at, user.twitter_username, user.get_starred().totalCount,user.get_repos().totalCount,user_language,user.email,c)
        counter+=1

      except:
        if  g.rate_limiting[0]==0:
          time_delay=(datetime.datetime.fromtimestamp(g.rate_limiting_resettime)-datetime.datetime.now()).total_seconds()+15
          mins,secs=divmod(time_delay,60)
          print(f'Error occurred in {counter} data fetch,Github rate exceeded,please wait {mins}:{secs}')
          utils.tools.countdown(time_delay)
          continue

        else:
          time_delay=10
          mins, secs = divmod(time_delay, 60)
          print(f'Error occurred in {counter} data fetch,connection lost,please wait {mins}:{secs}')
          utils.tools.countdown(time_delay)
          continue

  print(f'data for {counter} users fetched')


n=10
github_user_list=fetch_user(n)
start_time=time.time()
fetch_data(github_user_list)
finish_time=time.time()
print(finish_time-start_time)

with utils.context_managers.connection_handler() as conn:
  df=pd.read_sql_query("SELECT * FROM github_users",conn)
  print(df.head)

df.to_excel('Output Files/Github_data.xlsx',sheet_name='main',index=False)
