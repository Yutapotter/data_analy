import pandas as pd 

uselog=pd.read_csv("use_log.csv")

uselog["usedate"]=pd.to_datetime(uselog["usedate"])
uselog["年月"]=uselog["usedate"].dt.strftime("%Y/%m")
uselog_months=uselog.groupby(["年月","customer_id"],as_index=False).count()
uselog_months.rename(columns={"log_id":"count"},inplace=True)
del uselog_months["usedate"]
#print(uselog_months.head())

uselog_customer=uselog_months.groupby("customer_id").agg(["mean","median","max","min"])["count"]#aggは集計機能

uselog_customer=uselog_customer.reset_index(drop=False)

uselog["weekday"]=uselog["usedate"].dt.weekday#曜日を数字に変換
uselog_weekday=uselog.groupby(["customer_id","年月","weekday"],as_index=False).count()[["customer_id","年月","weekday","log_id"]]#特定のカラムを抽出
uselog_weekday.rename(columns={"log_id":"count"},inplace=True)#カラム名を変更

uselog_weekday=uselog_weekday.groupby("customer_id",as_index=False).max()[["customer_id","count"]]
uselog_weekday["routine_flg"]=0
uselog_weekday["routine_flg"]=uselog_weekday["routine_flg"].where(uselog_weekday["count"]<4,1)
print(uselog_weekday)