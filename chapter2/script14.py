import pandas as pd 

uriage_data=pd.read_csv("uriage.csv")
uriage_data["purchase_date"]=pd.to_datetime(uriage_data["purchase_date"]) 
uriage_data["purhcase_date"]=uriage_data["purchase_date"].dt.strftime("%Y/%m")

print(len(pd.unique(uriage_data.item_name)))

uriage_data["item_name"]=uriage_data["item_name"].str.upper()#小文字を大文字に変換
#全角・半角空欄を排除
uriage_data["item_name"]=uriage_data["item_name"].str.replace("　","")
uriage_data["item_name"]=uriage_data["item_name"].str.replace(" ","")
#item_nameで昇順に並び替え
uriage_data.sort_values(by=["item_name"],ascending=True,inplace=True)
print(uriage_data["item_name"])
print(pd.unique(uriage_data["item_name"]))
print(len(pd.unique(uriage_data["item_name"])))