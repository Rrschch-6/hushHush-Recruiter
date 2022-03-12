import sys
sys.path.append('C:/Users/Sasha/Documents/11-SRH Heidelberg/Big Data Programming Project/hushHush-Recruiter-Group-3/Scoring Algorithm/utils')

import pandas as pd
import utils

print(utils.Select_Candidate.step_1(table='Stack',id_column='UserID',name_column='UserName',email_column='UserEmail',score_column='Average'))
#print(utils.Select_Candidate.step_1('Github'))