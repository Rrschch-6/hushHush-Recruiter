
import pandas as pd





def select_attandee(n,r):
    df = pd.read_excel(r"C:\Users\oates\Downloads\labeled_data (1).xlsx")
    dffilterred=df[df["role"]==r]
    dffilterred_sorted=dffilterred.sort_values("weighted_score",ascending=False)
    print(dffilterred_sorted.iloc[0:n][["weighted_score","email","role"]])
    return dffilterred_sorted.iloc[0:n]["email"].values

