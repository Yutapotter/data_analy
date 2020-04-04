import pandas as pd
#売上データと顧客情報の読み込み
df1=pd.read_csv("uriage.csv")
df2=pd.read_excel("kokyaku_daicho.xlsx")

print(df1)
print(df2)
