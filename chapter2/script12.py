import pandas as pd 

uriage_data=pd.read_csv("uriage.csv")
#売上データの表示
print(uriage_data["item_name"][:20],uriage_data.item_price)