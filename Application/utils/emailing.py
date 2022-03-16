import smtplib
import sorting
import sys
import pandas as pd

def batch_email(df,n):

    df = df.sort_values(by="score_github", ascending=False)
    df=df.iloc[0:n, :]
    print(df.shape)
    email_list=df['email'].tolist()
    print(email_list)
    ADRESS="srhrecruiter1@gmail.com"
    PASSWORD="SRHrecruiter1"
    receiver=["sasha.behrouzi@gmail.com","sasha.behrouzi@gmail.com"]

    with smtplib.SMTP("smtp.gmail.com",587,timeout=100) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(ADRESS,PASSWORD)

        for i in email_list:
            subject="Congratilations you selected from SRHrecruiter"
            body="Please click the link attending our quiz: https://www.surveymonkey.de/r/MCCDFR3"
            msg=f'Subject:{subject}\n\n{body}'
            smtp.sendmail(ADRESS,i,msg)


batch_email(test_df,2)

