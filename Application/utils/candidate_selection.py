import sys
sys.path.append('C:/Users/Sasha/Documents/11-SRH Heidelberg/Big Data Programming Project/hushHush-Recruiter-Group-3/Application')
import pandas as pd
import utils

def algorithm_1(p1,p2,p3,df_main):
    df_main['weighted_score']=df_main['score_Github']+df_main['score_Kaggle']+df_main['score_Stack']+df_main['score_twitter']*0.5
    df_1=utils.tools.pick_top(df_main,'score_Github',percentile=p1)
    df_2=utils.tools.pick_top(df_main,'score_Kaggle',percentile=p1)
    df_3=utils.tools.pick_top(df_main, 'score_Stack', percentile=p1)
    df_solution_architecht= pd.concat([df_1,df_2,df_3])
    df_solution_architecht.drop_duplicates(subset=['email'],inplace=True)

    df_level_1=utils.tools.difference(df_main,df_solution_architecht)

    df_1=utils.tools.pick_top(df_level_1, 'score_Github', percentile=p2-p1)
    df_2=utils.tools.pick_top(df_level_1, 'score_Kaggle', percentile=p2-p1)
    df_3=utils.tools.pick_top(df_level_1, 'score_Stack', percentile=p2-p1)
    df_senior_developer = pd.concat([df_1, df_2, df_3])
    df_senior_developer.drop_duplicates(subset=['email'], inplace=True)

    df_level_2 = utils.tools.difference(df_level_1, df_senior_developer)

    df_1=utils.tools.pick_top(df_level_2, 'score_Github', percentile=p3-p2)
    df_2=utils.tools.pick_top(df_level_2, 'score_Kaggle', percentile=p3-p2)
    df_3=utils.tools.pick_top(df_level_2, 'score_Stack', percentile=p3-p2)
    df_developer = pd.concat([df_1, df_2, df_3])
    df_developer.drop_duplicates(subset=['email'], inplace=True)

    df_not_selected=utils.tools.difference(df_level_2, df_developer)

    df_additional_developers = utils.tools.pick_top(df_not_selected,'weighted_score', percentile=p1)

    df_developer.append(df_additional_developers)

    temp=pd.concat([df_solution_architecht,df_senior_developer,df_developer])
    df_not_selected=utils.tools.difference(df_main,temp)

    return df_solution_architecht,df_senior_developer,df_developer,df_not_selected

#SVM Machine Algorithm
def algorithm_2(df):

    import pandas as pd
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import MinMaxScaler, OrdinalEncoder
    from sklearn.metrics import accuracy_score, plot_confusion_matrix, confusion_matrix
    from matplotlib import pyplot as plt
    from sklearn.svm import SVC
    X = df[['score_github', 'score_normalised_kaggle',
            'score_stack', 'score_twitter', 'weighted_score']]
    Y = df.loc[:, 'role']
    # scaler = MinMaxScaler()
    # X = scaler.fit_transform(X)

    ordinal = OrdinalEncoder()
    Y = ordinal.fit_transform(Y.values.reshape(-1, 1))
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3)
    # plt.hist(Y)
    # plt.show()
    # clf = LogisticRegression(random_state=0 , max_iter = 3000).fit(X, Y)
    clf = SVC(decision_function_shape='ovo').fit(X_train, Y_train)
    # OVO: one versus one-OVR:one versus rest
    #
    predicted_labels = clf.predict(X_test)
    acc = accuracy_score(Y_test, predicted_labels)
    plot_confusion_matrix(clf, X, Y,
                          display_labels=['Developer', 'Not Selected', 'Senior Dev', 'Solution Architecht'], )
    cm = confusion_matrix(Y_test, predicted_labels)
    print("confusion_matrix\n " + '=' * 10)
    print(cm)
    print("Accuracy\n " + '=' * 10)
    print(acc)
    plt.show()

#NN
def algorithm_3(df):
    import pandas as pd
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import train_test_split
    from sklearn.neural_network import MLPClassifier
    from sklearn.preprocessing import MinMaxScaler, OrdinalEncoder
    from sklearn.metrics import accuracy_score, plot_confusion_matrix, confusion_matrix
    from matplotlib import pyplot as plt

    df = pd.read_excel("D:/UNI/Big_data/project/labeled_data (1).xlsx")
    df_train, df_test = train_test_split(df, test_size=0.3)
    X_train = df_train[['score_github', 'score_normalised_kaggle',
                        'score_stack', 'score_twitter', 'weighted_score']]
    Y_train = df_train.loc[:, ('role',)]
    X_test = df_test[['score_github', 'score_normalised_kaggle',
                      'score_stack', 'score_twitter', 'weighted_score']]
    Y_test = df_test.loc[:, ('role',)]

    # scaler = MinMaxScaler()
    # X = scaler.fit_transform(X)
    ordinal = OrdinalEncoder()
    Y_train = ordinal.fit_transform(Y_train)  # change y to numeric values
    Y_test = ordinal.transform(Y_test)  # change y to numeric values
    # plt.hist(Y)
    # plt.show()
    # clf = LogisticRegression(random_state=0 , max_iter = 3000).fit(X, Y)
    clf = MLPClassifier(solver='lbfgs', hidden_layer_sizes=(10, 2), random_state=1).fit(X_train,
                                                                                                    Y_train)  # Building neural network model
    predicted_labels = clf.predict(X_test)
    acc = accuracy_score(Y_test, predicted_labels)
    cm = confusion_matrix(Y_test, predicted_labels)
    print("confusion_matrix\n " + '=' * 10)
    print(cm)
    print("Accuracy\n " + '=' * 10)
    print(acc)
    plot_confusion_matrix(clf, X_test, Y_test,
                          display_labels=['Developer', 'Not Selected', 'Senior Dev', 'Solution Architecht'])
    plt.show()
    df_test = df_test.append(pd.Series(predicted_labels), ignore_index=True)
    print(df_test)
