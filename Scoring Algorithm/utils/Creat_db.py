import sys
sys.path.append('C:/Users/Sasha/Documents/11-SRH Heidelberg/Big Data Programming Project/hushHush-Recruiter-Group-3/Scoring Algorithm/utils')

import pandas as pd
import utils
import context_managers
import numpy
from sklearn import preprocessing
import sqlite3


Creat Databse
with utils.context_managers.cursor_handler() as c:
    c.execute('DROP TABLE Data_Source_GitHub')
    c.execute('DROP TABLE Data_Source_Stackoverflow')


with utils.context_managers.connection_handler() as conn:
    df_1=pd.read_excel('Data/Github_Data_with Score_8_March.xlsx')
    stack.to_sql(name='Data_Source_GitHub',con=conn,index=False)
    df_2=pd.read_csv('Data/StackData.csv')
    df_2.to_sql(name='Data_Source_Stackoverflow',con=conn,index=False)