import pandas as pd
import sqlite3
import csv

conn = sqlite3.connect('HushHush.db')
c = conn.cursor()


# select = 'select {id_column},{name_column},{email_column},{score_column} from {table} order by {score_column} desc'
# #df = pd.read_sql(select,conn)
# print(select)
def step2 ():
    table = 'stack'
    id_column = 'UserID'
    name_column = 'UserName'
    email_column = 'UserEmail'
    score_column = 'average'
    select = 'select {}  as UserID,{},{} from {} order by {} desc'.format(id_column,name_column,email_column,table,score_column)

    df = pd.read_sql(select, conn)

    TOP20 = int(round(len(df.index) * 0.2, 0))

    df_head20 = df.head(TOP20)
    #print(df.head(2))
    df_head50 = df.merge(df_head20, on=['UserID'])
    #print(df_head20.head(2))
    df[(~df[f'{id_column}'].isin(df_head50[f'{id_column}'])) & (~df[f'{id_column}'].isin(df_head50[f'{id_column}']))]
    #print(df_head50.head(2))
    df_head50.rename(columns={f"{name_column}_x": f"{name_column}", f"{email_column}_x": f"{email_column}"},inplace=True)
    df_head50 = df[[f'{id_column}',f'{name_column}',f'{email_column}']]

    TOP50 = int(round(len(df_head50.index) * 0.5, 0))

    df_head50 = df_head20.head(TOP50)
    #print(df_head50.head(2))
    return df_head50


#######################
def Priotrity2():
    table = 'twitter'
    id_column = 'UserID'
    name_column = 'UserName'
    email_column = 'UserEmail'
    score_column = 'average'
    select_t = 'select {} as UserID,{},{} from {} order by {} desc'.format(id_column, name_column, email_column, table,score_column)


    df_twitter = pd.read_sql(select_t, conn)
    TOP10 = int(round(len(df_twitter.index) * 0.1, 0))
    df_twitter10 = df_twitter.head(TOP20)
    return df_twitter10


######################## INNER JOIN BETWEEN PRIORITY 1 & 2#############

def joinPriority2(df_twitter10, df_head50):
    df_com = pd.merge(df_twitter10, df_head50, how="inner", on=["UserID"])

    [print(len(df_com.index))]

    return df_com

step2()