import pandas as pd 

uriage_data=pd.read_csv("uriage.csv")
uriage_data["purchase_date"]=pd.to_datetime(uriage_data.purchase_date)#datetime型に変更
uriage_data["purchase_date"]=uriage_data["purchase_date"].dt.strftime("%Y/%m")#月まで表示

#pivot_table
res1=pd.pivot_table(uriage_data,index="purchase_date",columns="item_name",aggfunc="count",fill_value=0)
res2=pd.pivot_table(uriage_data,index="purchase_date",columns="item_name",values="item_price",aggfunc="sum",fill_value=0)
print(res1,res2)