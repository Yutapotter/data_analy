import pandas as pd 

uriage_data=pd.read_csv("uriage.csv")
uriage_data["purchase_date"]=pd.to_datetime(uriage_data["purchase_date"])
uriage_data["purchase_date"]=uriage_data["purchase_date"].dt.strftime("%Y%m")

uriage_data["item_name"]=uriage_data["item_name"].str.replace(" ","")
uriage_data["item_name"]=uriage_data["item_name"].str.replace("　","")
uriage_data["item_name"]=uriage_data["item_name"].str.upper()
uriage_data.sort_values(by="item_name",ascending=True,inplace=True)
print(uriage_data.isnull().any(axis=0))

flg_is_null=uriage_data["item_price"].isnull()
for trg in list(uriage_data["item_name"].sort_values().unique()):
    print(trg+"の最大級:"+str(uriage_data.loc[uriage_data["item_name"]==trg]["item_price"].max())+"の最小値"+str(uriage_data.loc[uriage_data["item_name"]==trg]["item_price"].min(skipna=False)))
for trg in list(uriage_data.loc[flg_is_null,"item_name"].unique()):
    price=uriage_data.loc[(~flg_is_null)&(uriage_data["item_name"]==trg),"item_price"].max()
    uriage_data["item_price"].loc[(flg_is_null)&(uriage_data["item_name"]==trg)]=price

print(uriage_data.isnull().any(axis=0))

for trg in list(uriage_data["item_name"].sort_values().unique()):
    print(trg+"の最大級:"+str(uriage_data.loc[uriage_data["item_name"]==trg]["item_price"].max())+"の最小値"+str(uriage_data.loc[uriage_data["item_name"]==trg]["item_price"].min(skipna=False)))