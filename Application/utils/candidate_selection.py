import sys
sys.path.append('C:/Users/Sasha/Documents/11-SRH Heidelberg/Big Data Programming Project/hushHush-Recruiter-Group-3/Application')
import pandas as pd
import utils

def algorithm_1(p1,p2,p3,df_main):
    df_main['weighted_score']=df_main['score_github']+df_main['score_kaggle']+df_main['score_stack']+df_main['score_twitter']*0.5
    df_1=utils.tools.pick_top(df_main,'score_github',percentile=p1)
    df_2=utils.tools.pick_top(df_main,'score_kaggle',percentile=p1)
    df_3=utils.tools.pick_top(df_main, 'score_stack', percentile=p1)
    df_solution_architecht= pd.concat([df_1,df_2,df_3])
    df_solution_architecht.drop_duplicates(subset=['email'],inplace=True)

    df_level_1=utils.tools.difference(df_main,df_solution_architecht)

    df_1=utils.tools.pick_top(df_level_1, 'score_github', percentile=p2-p1)
    df_2=utils.tools.pick_top(df_level_1, 'score_kaggle', percentile=p2-p1)
    df_3=utils.tools.pick_top(df_level_1, 'score_stack', percentile=p2-p1)
    df_senior_developer = pd.concat([df_1, df_2, df_3])
    df_senior_developer.drop_duplicates(subset=['email'], inplace=True)

    df_level_2 = utils.tools.difference(df_level_1, df_senior_developer)

    df_1=utils.tools.pick_top(df_level_2, 'score_github', percentile=p3-p2)
    df_2=utils.tools.pick_top(df_level_2, 'score_kaggle', percentile=p3-p2)
    df_3=utils.tools.pick_top(df_level_2, 'score_stack', percentile=p3-p2)
    df_developer = pd.concat([df_1, df_2, df_3])
    df_developer.drop_duplicates(subset=['email'], inplace=True)

    df_not_selected=utils.tools.difference(df_level_2, df_developer)

    df_1 = utils.tools.pick_top(df_not_selected,'weighted_score', percentile=p1)
    df_2 = utils.tools.pick_top(df_not_selected,'weighted_score', percentile=p2)
    df_3 = utils.tools.pick_top(df_not_selected,'weighted_score', percentile=p3)

    df_solution_architecht.append(df_1)
    df_senior_developer.append(df_2)
    df_developer.append(df_3)
    temp=pd.concat([df_solution_architecht,df_senior_developer,df_developer])
    df_not_selected=utils.tools.difference(df_main,temp)

    return df_solution_architecht,df_senior_developer,df_developer,df_not_selected



