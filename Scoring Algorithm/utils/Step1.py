import pandas as pd
import sqlite3
import numpy

#import utils
print("Thi is my push")
conn = sqlite3.connect('HushHush.db')
c = conn.cursor()

######## in STEP1 each source top candidates are picked respective of other sources ##############
def step_1(table,id_column,name_column,email_column,score_column):
    #with utils.context_managers.connection_handler() as conn:

    select_query = "SELECT {},{},{},{} FROM {} order by {} desc".format(id_column,name_column,email_column,score_column,table,score_column)
    df = pd.read_sql(select_query,conn)

    #############Picking Senior Arcitect################

    Sen_Arch_Count =  int(round(len(df.index) * 0.1, 0))
    #print(Sen_Arch_Count)

    df_sen_arc = df.head(Sen_Arch_Count)
    # print(df_sen_arc.head(2))
    # print(df.head(2))

    #############Picking Senior Developers################

    df_common = df.merge(df_sen_arc, on=['UserID'])
    df_sen_dev_main = df[(~df.UserID.isin(df_common.UserID)) & (~df.UserID.isin(df_common.UserID))]

    Sen_Dev_Count = (int(round(len(df_sen_dev_main.index) * 0.20, 0)))
    df_sen_dev = df_sen_dev_main.head(Sen_Dev_Count)




    #############Picking Developers################

    df_common = df_sen_dev_main.merge(df_sen_dev, on=['UserID'])
    df_dev_main = df_sen_dev_main[(~df.UserID.isin(df_common.UserID)) & (~df.UserID.isin(df_common.UserID))]

    Dev_Count = (int(round(len(df_dev_main.index) * 0.25, 0)))
    df_dev = df_dev_main.head(Dev_Count)


    ############################ MERGING ALL THE CANDIDATES IN STEP1 #######################
    df_sen_arc.loc[:, 'Position'] = 'Senior Architect'
    df_sen_dev.loc[:, 'Position'] = 'Senior Developer'
    df_dev.loc[:, 'Position'] = 'Developer'
    df_union = pd.concat([df_sen_arc, df_sen_dev, df_dev], axis=0)
    return df_union
######## in STEP2  the above funcation need to be called 3 times as per our each source ##############
def step2(df_union):
    step_1('stack', 'UserId', 'username', 'useremail', 'score')
    df_stack = df_union
    #print(df_stack.head(2))
    #print('Stack loaded')
    step_1('Github', 'UserId', 'username', 'useremail', 'score')
    df_github = df_union
    #print(df_github.head(2))
    #print('GitHub loaded')
    step_1('Github', 'UserId', 'username', 'useremail', 'score')
    df_kaggle = df_union
    #print('Kaggle loaded.head(2)')

################## PICK the unique records from 3 data source  ##################


    df_kaggle_index = df_kaggle.set_index([0, 1]).index
    df_github_index = df_github.set_index([0, 1]).index
    df_mask = ~df_kaggle_index.isin(df_github_index)

    df_mask_index = df_mask.set_index([0, 1]).index
    df_stack_index = df_stack.set_index([0, 1]).index
    df_mask = ~df_mask_index.isin(df_stack_index)

    return df_mask
    ######## in STEP3  similar to STEP1 we picked all the source candiates irrespective of the scores in other source ##############
    ############ SIMILAR to SEP1 ##############
    ############# ALGORITHM 2  ################
def step_3(id_column,name_column,email_column,score_column,table):
    select_query = "SELECT {},{},{},{} FROM {} order by {} desc".format(id_column, name_column, email_column,
                                                                        score_column, table, score_column)
    df = pd.read_sql(select_query, conn)

    #############Picking Senior Arcitect################

    Sen_Arch_Count = int(round(len(df.index) * 0.25, 0))
    # print(Sen_Arch_Count)

    df_sen_arc = df.head(Sen_Arch_Count)

    # print(df_sen_arc.head(2))
    # print(df.head(2))

    #############Picking Senior Developers################

    df_common = df.merge(df_sen_arc, on=['UserID'])
    df_sen_dev_main = df[(~df.UserID.isin(df_common.UserID)) & (~df.UserID.isin(df_common.UserID))]

    Sen_Dev_Count = (int(round(len(df_sen_dev_main.index) * 0.30, 0)))
    df_sen_dev = df_sen_dev_main.head(Sen_Dev_Count)

    #############Picking Developers################

    df_common = df_sen_dev_main.merge(df_sen_dev, on=['UserID'])
    df_dev_main = df_sen_dev_main[(~df.UserID.isin(df_common.UserID)) & (~df.UserID.isin(df_common.UserID))]

    Dev_Count = (int(round(len(df_dev_main.index) * 0.40, 0)))
    df_dev = df_dev_main.head(Dev_Count)

    ############################ MERGING ALL THE CANDIDATES IN ALGORITHIM 2 #######################

    ######### ADDING THE EXTRA ATTRIBUTE MIN_AVG TO VERIFY AFTER MERGING EACH SOURCE THE SELECTION CRITERIA TO CHECK ON TWITTER IN CASE EQUALS TO CUT OF PERCENTILE ##########
    df_dev.assign(MIN_SCORE=lambda x: x.df_dev['Score'].min())
    df_sen_dev.assign(MIN_SCORE=lambda x: x.df_sen_arc['Score'].min())
    df_sen_arc.assign(MIN_SCORE=lambda x: x.df_sen_arc['Score'].min())

    df_sen_arc.loc[:, 'Position','Min_Average'] = 'Senior Architect'
    df_sen_dev.loc[:, 'Position'] = 'Senior Developer'
    df_dev.loc[:, 'Position'] = 'Developer'


    df_union = pd.concat([df_sen_arc, df_sen_dev, df_dev], axis=0)
    return df_union

######### IN STEP4 YOU MERGE ALL THE SOURCE , THEN VERIFY THE SELECTION CRITERIA FOR EACH POSITION  AND FINALLY USING MASK REMOVE THE SELECTED CANDIATES FROM STEP1/2 LIST ##########
def step4(df_union,df_mask):
    step_3('stack', 'UserId', 'username', 'useremail', 'score')
    df_stack = df_union
    # print(df_stack.head(2))
    # print('Stack loaded')
    step_1('Github', 'UserId', 'username', 'useremail', 'score')
    df_github = df_union
    # print(df_github.head(2))
    # print('GitHub loaded')
    step_1('Github', 'UserId', 'username', 'useremail', 'score')
    df_kaggle = df_union
    # print('Kaggle loaded.head(2)')
    step_1('Twitter', 'UserId', 'username', 'useremail', 'score')
    df_Twitter = df_union
    # print('Kaggle loaded.head(2)')
################## MERGE WITH OTHER SOURCE AND RENAMING   ##################

    # df_stack_github = pd.merge(df_stack,df_github,on='UserEmail',how='outer')
    # df_stack_github.rename(columns={"UserName_x": "UserName", "UserEmail_x": "UserEmail","Score_x"="Stack_Score","Score_y"="Github_Score","MIN_SCORE_x"="Stack_MIN_SCORE","MIN_SCORE_y"="Github_MIN_SCORE","POSITION_x"="Stack_Position","POSITION_y"="Github_Position"}, inplace=True)
    # df_stack_github = df[['UserID', 'UserName', 'UserEmail'],]


################## remove the candidates picked for algorithim1  ##################

    # df_algorithm2 = pd.concat([df_kaggle, df_stack, df_Twitter,df_github], axis=0)
    #
    # df_algorithm2_index = df_algorithm2.set_index([0, 1]).index
    # df_mask_index = df_mask.set_index([0, 1]).index
    # df_algorithm2_mask = ~df_algorithm2_index.isin(df_mask_index)


