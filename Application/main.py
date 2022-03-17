import sys
sys.path.append('C:/Users/Sasha/Documents/11-SRH Heidelberg/Big Data Programming Project/hushHush-Recruiter-Group-3/Scoring Algorithm/utils')
import sqlite3
import pandas as pd
import utils

number_of_applicants=5
role='Senior Developer'

df_main=utils.data_tools.merge()

if role == 'Solution Architect':
    df=utils.candidate_selection.algorithm_1(0.1,0.2,0.3,df_main)[0]
    email_list = utils.tools.select_mails(df, number_of_applicants)
    #utils.emailing.batch_email(email_list,number_of_candidates)
    print(email_list)

if role == 'Senior Developer':
    df = utils.candidate_selection.algorithm_1(0.1, 0.2, 0.3, df_main)[1]
    email_list = utils.tools.select_mails(df, number_of_applicants)
    #utils.emailing.batch_email(email_list,number_of_candidates)
    print(email_list)

if role == 'Developer':
    df = utils.candidate_selection.algorithm_1(0.1, 0.2, 0.3, df_main)[2]
    email_list = utils.tools.select_mails(df, number_of_applicants)
    #utils.emailing.batch_email(email_list,number_of_candidates)
    print(email_list)

email_dict={}
for i in range(len(email_list)):
    email_dict[f'Applicant {i + 1}->'] = email_list[i]
print(email_dict)

