import pandas as pd
import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi
import numpy as np
import random

#get_ipython().system('pip install kaggle')
api=KaggleApi()
api.authenticate()
kaggle.api.competitions_list()
x=kaggle.api.competitions_list()
print(x)
#Downloading leader dashboards
kaggle.api.competition_leaderboard_download("titanic", "download_leaderboard/leaderboard")



df1 = pd.read_csv(r"C:\Users\oates\OneDrive\Belgeler\Masters\Bigdata\DBs\competitive-data-science-predict-future-sales.zip",sep=",")
df2= pd.read_csv(r"C:\Users\oates\OneDrive\Belgeler\Masters\Bigdata\DBs\connectx.zip",sep=",")
df3=pd.read_csv(r"C:\Users\oates\OneDrive\Belgeler\Masters\Bigdata\DBs\contradictory-my-dear-watson.zip",sep=",")
df4=pd.read_csv(r"C:\Users\oates\OneDrive\Belgeler\Masters\Bigdata\DBs\digit-recognizer.zip",sep=",")
df5=pd.read_csv(r"C:\Users\oates\OneDrive\Belgeler\Masters\Bigdata\DBs\feedback-prize-2021.zip",sep=",")
df6=pd.read_csv(r"C:\Users\oates\OneDrive\Belgeler\Masters\Bigdata\DBs\tensorflow-great-barrier-reef.zip",sep=",")
df7=pd.read_csv(r"C:\Users\oates\OneDrive\Belgeler\Masters\Bigdata\DBs\ubiquant-market-prediction.zip",sep=",")
df8=pd.read_csv(r"C:\Users\oates\OneDrive\Belgeler\Masters\Bigdata\DBs\rsna-miccai-brain-tumor-radiogenomic-classification.zip",sep=",")
df9=pd.read_excel(r"C:\Users\oates\OneDrive\Belgeler\Masters\Bigdata\DBs\Sasha_Github.xlsx")
df9.info()
#tagging
df1["Score"]=df1["Score"]*100
df1["Tags"]="Prediction"
df2["Tags"]="Data Science"
df3["Tags"]="Data Science"
df4["Tags"]="Data Science"
df5["Tags"]="Data Science"
df6["Tags"]="Tensor Flow"
df7["Tags"]="Prediction"
df8["Tags"]="Classification"
# apply the min-max scaling in Pandas using the .min() and .max() methods
df1["Score_normalised"] = (df1["Score"] - df1["Score"].min()) / (df1["Score"].max() - df1["Score"].min())
df2["Score_normalised"] = (df2["Score"] - df2["Score"].min()) / (df2["Score"].max() - df2["Score"].min())
df3["Score_normalised"] = (df3["Score"] - df3["Score"].min()) / (df3["Score"].max() - df3["Score"].min())
df4["Score_normalised"] = (df4["Score"] - df4["Score"].min()) / (df4["Score"].max() - df4["Score"].min())
df5["Score_normalised"] = (df5["Score"] - df5["Score"].min()) / (df5["Score"].max() - df5["Score"].min())
df6["Score_normalised"] = (df6["Score"] - df6["Score"].min()) / (df6["Score"].max() - df6["Score"].min())
df7["Score_normalised"] = (df7["Score"] - df7["Score"].min()) / (df7["Score"].max() - df7["Score"].min())
df8["Score_normalised"] = (df8["Score"] - df8["Score"].min()) / (df8["Score"].max() - df8["Score"].min())

dfmain=pd.concat([df1,df2,df3,df4,df5,df6,df7,df8])
print(dfmain.info())
dfmain.columns.value_counts()# 19925
len(dfmain.index)
total_rows = dfmain.shape[0]
print("1",total_rows)




dfmain = dfmain[(dfmain['Score_normalised'] >= 0) & (dfmain['Score_normalised'] <= 1)]



q1=np.percentile(dfmain.Score, 25)  # Q1
q2=np.percentile(dfmain.Score, 50)  # median
q3=np.percentile(dfmain.Score, 75)  # Q3
print("first",q1,q1,q3)
print(dfmain.Score.describe())

print(dfmain.sort_values("Score",ascending=False))

#Data Cleaning

def outlier_thresholds(dataframe, variable):
    quartile1 = dataframe[variable].quantile(0.01)
    quartile3 = dataframe[variable].quantile(0.90)
    interquantile_range = quartile3 - quartile1
    up_limit = quartile3 + 1.5 * interquantile_range
    low_limit = quartile1 - 1.5 * interquantile_range
    return low_limit, up_limit

def replace_with_thresholds(dataframe, variable):
    low_limit, up_limit = outlier_thresholds(dataframe, variable)
    dataframe.loc[(dataframe[variable] < low_limit), variable] = low_limit
    dataframe.loc[(dataframe[variable] > up_limit), variable] = up_limit
replace_with_thresholds(dfmain,"Score_normalised")

print(dfmain.describe())
q1_new=np.percentile(dfmain.Score_normalised, 25)  # Q1
q2_new=np.percentile(dfmain.Score_normalised, 50)  # median
q3_new=np.percentile(dfmain.Score_normalised, 75)  # Q3
dfmain["Q1"]=q1_new
dfmain["Q2"]=q2_new
dfmain["Q3"]=q3_new
print(dfmain)



dfmain.to_excel('dbslasttoday.xlsx')

print(dfmain["Score_normalised"].describe())
print(dfmain["Score_normalised"]>0)