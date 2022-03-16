import sys
sys.path.append('C:/Users/Sasha/Documents/11-SRH Heidelberg/Big Data Programming Project/hushHush-Recruiter-Group-3/Scoring Algorithm/utils')
import sqlite3
import pandas as pd
import utils

number_of_candidates=5
role='Solution Architect'
df_input=pd.read_excel("all.xlsx")

if role == 'Solution Architect':
    email_list=utils.candidate_selection.algorithm_1(0.1,0.2,0.3,df_input)[0]
    utils.emailing.batch_email(email_list,number_of_candidates)
if role == 'Senior Developer':
    email_list=utils.candidate_selection.algorithm_1(0.1,0.2,0.3,df_input)[1]
    utils.emailing.batch_email(email_list,number_of_candidates)
if role == 'Developer':
    email_list=utils.candidate_selection.algorithm_1(0.1,0.2,0.3,df_input)[2]
    utils.emailing.batch_email(email_list,number_of_candidates)
