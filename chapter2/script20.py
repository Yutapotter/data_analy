import pandas as pd

import_data=pd.read_csv("dump_data.csv")
import_data["purchase_date"]=pd.to_datetime(import_data["purchase_date"])
import_data["purchase_month"]=import_data["purchase_date"].dt.strftime("%Y/%m")
import_data=import_data[["purchase_date","purchase_month","item_name","item_price","顧客名","かな","地域","メールアドレス","登録日"]]

print(import_data)