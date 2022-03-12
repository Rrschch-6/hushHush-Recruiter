import sys
sys.path.append('C:/Users/Sasha/Documents/11-SRH Heidelberg/Big Data Programming Project/hushHush-Recruiter-Group-3/Scoring Algorithm/utils')

import pandas as pd
import utils
import csv

def step_1(table,id_column,name_column,email_column,score_column):
    with utils.context_managers.connection_handler() as conn:
        select = f'select {id_column},{name_column},{email_column} from {table} order by {score_column} desc'
        df = pd.read_sql(select,conn)

    #Top 5 Pick
    #print(len(df.index))
    TOP5 = int(round(len(df.index)*0.05,0))
    df_head5 = df.head(TOP5)
    print('we have filtered top 5 s,develoeprs')
    #===================================================================
    #Top 10 Pick
    df_head10 = df.merge(df_head5,on=[f'{id_column}'])
    print(df_head10.columns)
    df[(~df[f'{id_column}'].isin(df_head10[f'{id_column}']))&(~df[f'{id_column}'].isin(df_head10[f'{id_column}']))]


    df_head10.rename(columns={f"{name_column}_x": f"{name_column}", f"{email_column}_x": f"{email_column}"}, inplace=True)
    df_head10= df[[f'{id_column}',f'{name_column}',f'{email_column}']]
    TOP10 = (int(round(len(df_head10.index)*0.10,0)))
    df=df_head10
    df_head10 = df_head10.head(TOP10)
    print('we have filtered top 10 s,develoeprs')
    # ===================================================================
    #Top 20 Pick

    df_head20 = df.merge(df_head5,on=[f'{id_column}'])
    print(df_head20.columns)
    df[(~df[f'{id_column}'].isin(df_head10[f'{id_column}']))&(~df[f'{id_column}'].isin(df_head10[f'{id_column}']))]


    df_head20.rename(columns={f"{name_column}_x": f"{name_column}", f"{email_column}_x": f"{email_column}"}, inplace=True)
    df_head20= df[[f'{id_column}',f'{name_column}',f'{email_column}']]

    TOP20 = (int(round(len(df_head20.index)*0.20,0)))
    df_head20 = df_head10.head(TOP20)

    print('we have filtered top 20 s,develoeprs')
    #==============================================================
    #consolidate all dfs together as a result
    df_head5['Position'] = 'Senior Architect'
    df_head10['Position'] = 'Senior Developer'
    df_head20['Position'] = 'Developer'
    df_union = pd.concat([df_head5,df_head10,df_head20],axis=0)


    return df_union




