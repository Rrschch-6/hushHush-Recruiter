import sys
sys.path.append('C:/Users/Sasha/Documents/11-SRH Heidelberg/Big Data Programming Project/hushHush-Recruiter-Group-3/Application')
import utils
import pandas as pd
import smtplib

#picks dataframe from HushHush database and unifies the column name
def pick_df(table,id_column,name_column,email_column,score_column):
    with utils.context_managers.connection_handler() as conn:
        select = f'select {id_column},{name_column},{email_column},{score_column} from {table} order by {score_column} desc'
        df_result = pd.read_sql(select,conn)

    df_result=df_result.rename(columns={f'{id_column}':'id',f'{name_column}':'user_name',f'{email_column}':'email',f'{score_column}':f'score_{table}'})
    df_result=df_result.dropna(subset=['email'])
    return df_result

#picks top precentile of input data frame according to specific column
def pick_top(df,column,percentile):
    df.sort_values(by=f'{column}', ascending=False)
    top= int(round(len(df.index)*percentile,0))
    df_result= df.head(top).copy()
    df_result=df_result.dropna(subset=['email']).copy()
    return df_result

#returns df2-df1
def difference(df1,df2):
    df=pd.concat([df1,df2])
    df_result=df.drop_duplicates(subset=['email'],keep=False)
    return df_result

#returns intersection of df1 and df2
def intersection(df1,df2):
    df=df1.merge(df2,how='inner',on='email')
    df=df.drop(columns=['id_y','user_name_y','score_y'])
    df_result=df.rename(columns={'id_x':'id','user_name_x':'user_name','score_x':'score'})
    return df_result

#selects n emails from df and returns a list
def select_mails(df,number_of_applicants):
    df = df.sort_values(by="weighted_score", ascending=False)
    df = df.iloc[0:number_of_applicants, :]
    email_list = df['email'].tolist()
    return email_list

#sends email to email_list
def batch_email(email_list):
    ADRESS="srhrecruiter1@gmail.com"
    PASSWORD="SRHrecruiter1"
    receiver=["sasha.behrouzi@gmail.com","sasha.behrouzi@gmail.com"]

    with smtplib.SMTP("smtp.gmail.com",587,timeout=100) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(ADRESS,PASSWORD)

        for i in email_list:
            subject="Job Alert from hushHush Recruiter!"

            body="""Congratulations! You've been selected for Doodle Foobar Challenge!
            To participate in the challenge, please click on the link below:
            https://www.surveymonkey.de/r/MCCDFR3
            We wish you all the good luck!!
                
            Cheers,
            Team Doodle"""

            msg=f'Subject:{subject}\n\n{body}'
            smtp.sendmail(ADRESS,i,msg)

batch_email(['oatesch@gmail.com','sasha.behrouzi@gmail.com'])