import sys
sys.path.append('C:/Users/Sasha/Documents/11-SRH Heidelberg/Big Data Programming Project/hushHush-Recruiter-Group-3/Application/utils')

import pandas as pd


def pick_df(table,id_column,name_column,email_column,score_column):
    with utils.context_managers.connection_handler() as conn:
        select = f'select {id_column},{name_column},{email_column},{score_column} from {table} order by {score_column} desc'
        df_result = pd.read_sql(select,conn)

    df_result=df_result.rename(columns={f'{id_column}':'id',f'{name_column}':'user_name',f'{email_column}':'email',f'{score_column}':'score'})
    df_result=df_result.dropna(subset=['email'])
    return df_result

def pick_top(df,column,percentile):
    df.sort_values(by=f'{column}', ascending=False)
    top= int(round(len(df.index)*percentile,0))
    df_result= df.head(top).copy()
    df_result=df_result.dropna(subset=['email']).copy()
    return df_result

def difference(df1,df2):
    df=pd.concat([df1,df2])
    df_result=df.drop_duplicates(subset=['email'],keep=False)
    return df_result

def intersection(df1,df2):
    df=df1.merge(df2,how='inner',on='email')
    df=df.drop(columns=['id_y','user_name_y','score_y'])
    df_result=df.rename(columns={'id_x':'id','user_name_x':'user_name','score_x':'score'})
    return df_result
