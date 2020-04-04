import pandas as pd 

kokyaku_data=pd.read_excel("kokyaku_daicho.xlsx")
uriage_data=pd.read_csv("uriage.csv")

flg_is_serial=kokyaku_data["登録日"].astype("str").str.isdigit()#全て文字列に変換し、その中で数字がどれか判別
flg_is_serial.sum()

fromSerial=pd.to_timedelta(kokyaku_data.loc[flg_is_serial,"登録日"].astype("float"),unit="D")+pd.to_datetime("1900/01/01")#unit="D"がないと時間まで表示される
print(fromSerial)

fromString=pd.to_datetime(kokyaku_data.loc[~flg_is_serial,"登録日"])#datetimeに変換

kokyaku_data["登録日"]=pd.concat([fromSerial,fromString])
print(kokyaku_data)

kokyaku_data["登録年月"]=kokyaku_data["登録日"].dt.strftime("%Y/%m")
rslt=kokyaku_data.groupby("登録年月").count()["顧客名"]
print(rslt,len(kokyaku_data))

flg_is_serial=kokyaku_data["登録日"].astype("str").str.isdigit()
print(flg_is_serial.sum())