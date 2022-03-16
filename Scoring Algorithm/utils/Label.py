import sys
sys.path.append('C:/Users/Sasha/Documents/11-SRH Heidelberg/Big Data Programming Project/hushHush-Recruiter-Group-3/Scoring Algorithm/utils')
import pandas as pd



df=pd.read_excel("all.xlsx")

df['score_github'] = df['score_github'] .fillna(0)
df['score_stack'] = df['score_stack'] .fillna(0)
df['score_normalised_kaggle'] = df['score_normalised_kaggle'] .fillna(0)
df['score_twitter'] = df['score_twitter'] .fillna(0)

for i in range(len(df)):
    print('\r', i, end=" ")
    df.loc[i,'weighted_score']=(df.loc[i,'score_github']+df.loc[i,'score_normalised_kaggle']+df.loc[i,'score_stack']+df.loc[i,'score_twitter']*0.5)
    if df.loc[i,'score_github']>df.quantile(.95,axis=0)[1] or df.loc[i,'score_normalised_kaggle']>df.quantile(.95,axis=0)[2] or df.loc[i,'score_stack']>df.quantile(.95,axis=0)[3] :
        df.loc[i,'role']='Solution Architecht'
    elif df.quantile(.9,axis=0)[1]<df.loc[i,'score_github']<df.quantile(.95,axis=0)[1] or df.quantile(.9,axis=0)[2]<df.loc[i,'score_normalised_kaggle']<df.quantile(.95,axis=0)[2] or df.quantile(.9,axis=0)[3]<df.loc[i,'score_stack']<df.quantile(.95,axis=0)[3]:
        df.loc[i,'role']='Senior Developer'
    elif df.quantile(.85,axis=0)[1]<df.loc[i,'score_github']<df.quantile(.9,axis=0)[1] or df.quantile(.85,axis=0)[2]<df.loc[i,'score_normalised_kaggle']<df.quantile(.9,axis=0)[2] or df.quantile(.85,axis=0)[3]<df.loc[i,'score_stack']<df.quantile(.9,axis=0)[3]:
        df.loc[i,'role']='Developer'
    else:
        df.loc[i, 'role'] = 'NA'

df_algorithm_1=df.loc[df['role'] != 'NA'].copy()
temp=df.loc[df['role'] == 'NA'].copy()
temp.to_excel('temp.xlsx')
df_algorithm_2=pd.read_excel("temp.xlsx")

for i in range(len(df_algorithm_2)):
    print('\r', i, end="")
    if df_algorithm_2.loc[i,'weighted_score']>df_algorithm_2.quantile(.95,axis=0)[6]:
        df_algorithm_2.loc[i,'role']='Solution Architecht'
    elif df_algorithm_2.quantile(.9,axis=0)[6]<df_algorithm_2.loc[i,'weighted_score']<df_algorithm_2.quantile(.95,axis=0)[6]:
        df_algorithm_2.loc[i,'role']='Senior Developer'
    elif df_algorithm_2.quantile(.85, axis=0)[6] < df_algorithm_2.loc[i, 'weighted_score'] < df_algorithm_2.quantile(.95, axis=0)[6]:
        df_algorithm_2.loc[i,'role']='Developer'
    else:
        df_algorithm_2.loc[i, 'role'] = 'Not Selected'

df_labeled=pd.concat([df_algorithm_1,df_algorithm_2],ignore_index=True)
df_labeled.to_excel('label.xlsx')

