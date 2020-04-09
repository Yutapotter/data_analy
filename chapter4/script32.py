import pandas as pd 
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


#csvファイルの読み込み
path1="customer_join.csv"
path2="use_log.csv"

customer=pd.read_csv(path1)
uselog=pd.read_csv(path2)

#顧客クラスタリングのために、必要カラム(月内利用履歴)を選択
customer_clustering=customer[["mean","median","max","min","membership_period"]]
#print(customer_clustering.head())

#クラスタリング

sc=StandardScaler()
customer_clustering_sc=sc.fit_transform(customer_clustering)#customer_ckusteringの値を標準化している。fitで期待値・分散を計算、transformで標準化した値を配列に反映

kmeans=KMeans(n_clusters=4,random_state=0)#クラスター数を四つに設定
clusters=kmeans.fit(customer_clustering_sc)#kmeansメソッドに標準化した値を代入
customer_clustering["cluster"]=clusters.labels_#クラスター結果：ラベルを取得
print(customer_clustering["cluster"].unique())
print(customer_clustering.head())
print(customer_clustering_sc)