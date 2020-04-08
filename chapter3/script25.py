import pandas as pd 

uselog=pd.read_csv("use_log.csv")

uselog["usedate"]=pd.to_datetime(uselog["usedate"])
uselog["年月"]=uselog["usedate"].dt.strftime("%Y/%m")
uselog_months=uselog.groupby(["年月","customer_id"],as_index=False).count()
uselog_months.rename(columns={"log_id":"count"},inplace=True)
del uselog_months["usedate"]
#print(uselog_months.head())

uselog_customer=uselog_months.groupby("customer_id").agg(["mean","median","max","min"])
uselog_customer1=uselog_months.groupby("customer_id").agg(["mean","median","max","min"])["count"]

uselog_customer=uselog_customer.reset_index(drop=False)
