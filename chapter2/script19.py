import pandas as pd 

kokyaku_data=pd.read_excel("kokyaku_daicho.xlsx")
uriage_data=pd.read_csv("uriage.csv")

flg_is_serial=kokyaku_data["登録日"].astype("str").str.isdigit()#全て文字列に変換し、その中で数字がどれか判別
flg_is_serial.sum()

fromSerial=pd.to_timedelta(kokyaku_data.loc[flg_is_serial,"登録日"].astype("float"),unit="D")+pd.to_datetime("1900/01/01")#unit="D"がないと時間まで表示される
#print(fromSerial)

fromString=pd.to_datetime(kokyaku_data.loc[~flg_is_serial,"登録日"])#datetimeに変換

kokyaku_data["登録日"]=pd.concat([fromSerial,fromString])
#print(kokyaku_data)

kokyaku_data["登録年月"]=kokyaku_data["登録日"].dt.strftime("%Y/%m")
rslt=kokyaku_data.groupby("登録年月").count()["顧客名"]
#print(rslt,len(kokyaku_data))

flg_is_serial=kokyaku_data["登録日"].astype("str").str.isdigit()
#print(flg_is_serial.sum())
uriage_data=pd.read_csv("uriage.csv")
uriage_data["purchase_date"]=pd.to_datetime(uriage_data["purchase_date"])
uriage_data["purchase_date"]=uriage_data["purchase_date"].dt.strftime("%Y%m")

uriage_data["item_name"]=uriage_data["item_name"].str.replace(" ","")
uriage_data["item_name"]=uriage_data["item_name"].str.replace("　","")
uriage_data["item_name"]=uriage_data["item_name"].str.upper()
uriage_data.sort_values(by="item_name",ascending=True,inplace=True)
#print(uriage_data.isnull().any(axis=0))

flg_is_null=uriage_data["item_price"].isnull()
for trg in list(uriage_data["item_name"].sort_values().unique()):
    print(trg+"の最大級:"+str(uriage_data.loc[uriage_data["item_name"]==trg]["item_price"].max())+"の最小値"+str(uriage_data.loc[uriage_data["item_name"]==trg]["item_price"].min(skipna=False)))
for trg in list(uriage_data.loc[flg_is_null,"item_name"].unique()):
    price=uriage_data.loc[(~flg_is_null)&(uriage_data["item_name"]==trg),"item_price"].max()
    uriage_data["item_price"].loc[(flg_is_null)&(uriage_data["item_name"]==trg)]=price

#print(uriage_data.isnull().any(axis=0))

for trg in list(uriage_data["item_name"].sort_values().unique()):
    print(trg+"の最大級:"+str(uriage_data.loc[uriage_data["item_name"]==trg]["item_price"].max())+"の最小値"+str(uriage_data.loc[uriage_data["item_name"]==trg]["item_price"].min(skipna=False)))

kokyaku_data["顧客名"]=kokyaku_data["顧客名"].str.replace(" ","")
kokyaku_data["顧客名"]=kokyaku_data["顧客名"].str.replace("　","")

join_data=pd.merge(uriage_data,kokyaku_data,left_on="customer_name",right_on="顧客名",how="left")
join_data=join_data.drop("customer_name",axis=1)

dump_data=join_data[["purchase_date","item_name","item_price","顧客名","かな","地域","メールアドレス","登録日"]]
print(dump_data)
dump_data.to_csv("dump_data.csv",index=False)