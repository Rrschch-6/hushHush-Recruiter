import pandas as pd
github = pd.read_excel(r"C:\Users\oates\OneDrive\Belgeler\Masters\Bigdata\github_1.xlsx")
kaggle = pd.read_excel(r"C:\Users\oates\OneDrive\Belgeler\Masters\Bigdata\kaggle_1.xlsx")
twitter = pd.read_excel(r"C:\Users\oates\OneDrive\Belgeler\Masters\Bigdata\twitter_1.xlsx")
stack = pd.read_excel(r"C:\Users\oates\OneDrive\Belgeler\Masters\Bigdata\stack_1.xlsx")
print("twitter",twitter.head())
print("kaggle",kaggle.head())
print("stack",stack.head())
print("github",github.head())

df1=github.merge(kaggle,left_on="email"
                 ,right_on="email",
                how="outer")
print(df1.info())

print("df1",df1.head())
df2=df1.merge(stack,left_on="email",
              right_on="email",
              how="outer")
print("df2",df2.head())
df3=df2.merge(twitter,left_on="email",
              right_on="email",
              how="outer")

df3.to_excel("all_merged.xlsx")

print(df3.head())
print(df3)