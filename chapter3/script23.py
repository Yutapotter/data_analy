import pandas as pd 

uselog=pd.read_csv("use_log.csv")
customer=pd.read_csv("customer_master.csv")
class_master=pd.read_csv("class_master.csv")
campaign_master=pd.read_csv("campaign_master.csv")

#customer,class,campaignをjoin
customer_join=pd.merge(customer,class_master,on="class",how="left")
customer_join=pd.merge(customer_join,campaign_master,on="campaign_id",how="left")
"""
print(customer_join.groupby("class_name").count()["customer_id"])
print(customer_join.groupby("gender").count()["customer_id"])
print(customer_join.groupby("campaign_name").count()["customer_id"])
print(customer_join.groupby("is_deleted").count()["customer_id"])"""

customer_join["start_date"]=pd.to_datetime(customer_join["start_date"])
customer_start=customer_join.loc[customer_join["start_date"]>pd.to_datetime("20180401")]
print(len(customer_start))