import pandas as pd
def question_4(df1, df2):
    new_set = pd.merge(df1, df2, on='学生姓名')
    return new_set
df1 = pd.read_excel("object-1-2-1.xlsx")
df2 = pd.read_excel("object-1-2-2.xlsx")
merged_df = question_4(df1, df2)
print(merged_df)
