import pandas as pd 

uselog=pd.read_csv("use_log.csv")
customer=pd.read_csv("customer_master.csv")
class_master=pd.read_csv("class_master.csv")
campaign_master=pd.read_csv("campaign_master.csv")

#customer,class,campaignをjoin
customer_join=pd.merge(customer,class_master,on="class",how="left")
customer_join=pd.merge(customer_join,campaign_master,on="campaign_id",how="left")


#start_dateをdatetimeに変換
customer_join["start_date"]=pd.to_datetime(customer_join["start_date"])
customer_start=customer_join.loc[customer_join["start_date"]>pd.to_datetime("20180401")]


customer_join["end_date"]=pd.to_datetime(customer_join["end_date"])
customer_newer=customer_join.loc[(customer_join["end_date"]>=pd.to_datetime("20190331"))|(customer_join["end_date"].isnull())]#isnaはisnullのエイリアス
print(len(customer_newer))
print(customer_newer["end_date"].unique())
print(customer_newer.groupby("class_name").count()["customer_id"])
print(customer_newer.groupby("campaign_name").count()["customer_id"])
print(customer_newer.groupby("gender").count()["customer_id"])
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

customer_join=pd.merge(customer_join,uselog_customer,on="customer_id",how="left")
customer_join=pd.merge(customer_join,uselog_weekday[["customer_id","routine_flg"]],on="customer_id",how="left")
print(customer_join.head())
print(customer_join.isnull().sum())