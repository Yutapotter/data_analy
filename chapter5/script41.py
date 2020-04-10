import pandas as pd
"""ファイルの読み込み"""

customer=pd.read_csv("customer_join.csv")
uselog_months=pd.read_csv("use_log_months.csv")

"""重複排除年月のリストを作り、各月の当月・前月利用回数を求める"""
year_months=list(uselog_months["年月"].unique())#年月だけを取り出す
uselog=pd.DataFrame()
for i in range(1,len(year_months)):
  tmp=uselog_months.loc[uselog_months["年月"]==year_months[i]]#5月から最新月の一月前まで
  tmp.rename(columns={"count":"count_0"},inplace=True)
  tmp_before=uselog_months.loc[uselog_months["年月"]==year_months[i-1]]
  del tmp_before["年月"]
  tmp_before.rename(columns={"count":"count_1"},inplace=True)
  tmp=pd.merge(tmp,tmp_before,on="customer_id",how="left")
  uselog=pd.concat([uselog,tmp],ignore_index=True)#ラベルを貼り直す
print(uselog.head())

