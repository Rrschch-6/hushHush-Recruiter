 def step_1():
    df_stack=utils.tools.pick_df(table='Stack',id_column='UserID',name_column='UserName',email_column='UserEmail',score_column='Average')
    df_git=utils.tools.pick_df(table='Github',id_column='user_list',name_column='user_name',email_column='user_email',score_column='score')
    df_kaggle=utils.tools.pick_df(table='Kaggle',id_column='user_list',name_column='user_name',email_column='user_email',score_column='score')

    df_stack_5=utils.tools.pick_top(df=df_stack,percentile=0.05)
    df_git_5 = utils.tools.pick_top(df=df_git, percentile=0.05)
    df_kaggle_5 = utils.tools.pick_top(df=df_git, percentile=0.05)

    df_architect=pd.concat([df_stack_5,df_git_5,df_kaggle_5]).drop_duplicates(subset=['email'])

    df_stack_10=utils.tools.pick_top(utils.tools.difference(df_stack_5,df_stack),percentile=0.1)
    df_git_10 = utils.tools.pick_top(utils.tools.difference(df_stack_5, df_stack), percentile=0.1)
    df_kaggle_10 = utils.tools.pick_top(utils.tools.difference(df_stack_5, df_stack), percentile=0.1)

    df_senior = pd.concat([df_stack_10, df_git_10, df_kaggle_10]).drop_duplicates(subset=['email'])


    df_stack_10 = utils.tools.pick_top(utils.tools.difference(df_stack_5, df_stack), percentile=0.1)
    df_git_10 = utils.tools.pick_top(utils.tools.difference(df_stack_5, df_stack), percentile=0.1)
    df_kaggle_10 = utils.tools.pick_top(utils.tools.difference(df_stack_5, df_stack), percentile=0.1)

    df_developer = pd.concat([df_stack_10, df_git_10, df_kaggle_10]).drop_duplicates(subset=['email'])


