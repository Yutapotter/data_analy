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