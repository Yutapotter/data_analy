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
uselog.head()
from dateutil.relativedelta import relativedelta

exit_customer=customer.loc[customer["is_deleted"]==1]
exit_customer["exit_date"]=None
exit_customer["end_date"]=pd.to_datetime(exit_customer["end_date"])
for i in range(len(exit_customer)):
  exit_customer["exit_date"].iloc[i]=exit_customer["end_date"].iloc[i]-relativedelta(months=1)#前月をexit_dateにしている
exit_customer["年月"]=exit_customer["exit_date"].dt.strftime("%Y%m")
uselog["年月"]=uselog["年月"].astype(str)
exit_uselog=pd.merge(uselog,exit_customer,on=["customer_id","年月"],how="left")
exit_uselog=exit_uselog.dropna(subset=["name"])
print(len(exit_uselog))
print(len(exit_uselog["customer_id"].unique()))
exit_uselog.head()
exit_uselog = exit_uselog.dropna(subset=["name"])
print(len(exit_uselog))
print(len(exit_uselog["customer_id"].unique()))
exit_uselog.head()
conti_customer=customer.loc[customer["is_deleted"]==0]
conti_uselog=pd.merge(uselog,conti_customer,on="customer_id",how="left")
conti_uselog=conti_uselog.dropna(subset=["name"])
print(conti_uselog)

conti_uselog=conti_uselog.sample(frac=1).reset_index(drop=True)
conti_uselog=conti_uselog.drop_duplicates(subset="customer_id")
print(len(conti_uselog))

predict_data=pd.concat([conti_uselog,exit_uselog],ignore_index=True)
predict_data.head()
print(len(predict_data))
predict_data["period"]=0
predict_data["now_date"]=pd.to_datetime(predict_data["年月"],format="%Y%m")
predict_data["start_date"]=pd.to_datetime(predict_data["start_date"])
for i in range(len(predict_data)):
    delta=relativedelta(predict_data["now_date"][i],predict_data["start_date"][i])
    predict_data["period"][i]=int(delta.years*12+delta.months)
predict_data.head()
predict_data.isna().sum()
predict_data=predict_data.dropna(subset=["count_1"])
predict_data.isna().sum()