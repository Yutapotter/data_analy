import pandas as pd 

uselog=pd.read_csv("use_log.csv")
customer=pd.read_csv("customer_master.csv")
class_master=pd.read_csv("class_master.csv")
campaign_master=pd.read_csv("campaign_master.csv")

customer_join=pd.merge(customer,class_master,on="class",how="left")
customer_join=pd.merge(customer_join,campaign_master,on="campaign_id",how="left")
print(customer_join.head(),len(customer),len(customer_join))
print(customer_join.isnull().any(axis=0))#欠損値の確認