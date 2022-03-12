import time
import context_managers
import sqlite3


def countdown(t):
  while t:
    mins, secs = divmod(t, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print('\r',f'please wait for {timer}',end='')
    time.sleep(1)
    t -= 1
  print('',end='\r')

#sqlite3 tools
def create_table(table,c):
    c.execute(f""" CREATE TABLE IF NOT EXISTS {table}(
                user_list text,
                user_name text,
                user_followers integer,
                user_created_at text,
                user_twitter_username text,
                user_stars integer,
                user_repos integer,
                user_language text,
                user_email text
                )""")
    
def insert_user(table,user_name,user_credentials,followers,user_created_at,user_twitter_account,user_stars,user_repos,user_language,user_email,c):
        c.execute(f"INSERT into {table} VALUES (:user_name,:user_credentials,:followers,:user_created_at,:user_twitter_account,:user_stars,:user_repos,:user_language,:user_email)",
                {'user_name':user_name,'user_credentials':user_credentials,'followers':followers,'user_created_at':user_created_at,'user_twitter_account':user_twitter_account,'user_stars':user_stars,'user_repos':user_repos,'user_language':user_language,'user_email':user_email})

def get_user_by_name(table,user_name,c):
  c.execute(f"SELECT * FROM {table} WHERE user_name=:user_name", {'user_name':user_name})
  c.fetchall()


def update(table, user_name, x,c):
    c.execute(f"""UPDATE {table} SET {x}=:x
                    WHERE user_id=:user_id""",
              {'user_name':user_name,'x': x})

def remove_user(table, user_id,c):
    c.execute(f"DELETE from {table} WHERE user_id=:user_name",
                  {'user_name' :user_name})
    
def table_count(table,c):
    c.execute(f"SELECT COUNT(*) FROM {table}")
    return c.fetchone()

#spliting list to smaller chunks

def splitList(list, chunkSize):
  return [list[i:i + chunkSize] for i in range(0, len(list), chunkSize)]


