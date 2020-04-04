import pandas as pd 

kokyaku_data=pd.read_excel("kokyaku_daicho.xlsx")
uriage_data=pd.read_csv("uriage.csv")

print(kokyaku_data["顧客名"].head(),uriage_data["customer_name"])

#顧客データの全角半角スペースを除去
kokyaku_data["顧客名"]=kokyaku_data["顧客名"].str.replace(" ","")
kokyaku_data["顧客名"]=kokyaku_data["顧客名"].str.replace("　","")
print(kokyaku_data["顧客名"].head())
