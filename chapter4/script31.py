import pandas as pd  

#csvファイルの読み込み
path1="customer_join.csv"
path2="use_log.csv"

customer=pd.read_csv(path1)
uselog=pd.read_csv(path2)

print(customer.isnull().sum(),uselog.isnull().sum())