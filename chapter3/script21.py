import pandas as pd 


path=["use_log.csv","customer_master.csv","class_master.csv","campaign_master.csv"]

for data in path:
    df=pd.read_csv(data)
    print(len(df))
    print(df.head())

