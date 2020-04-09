import  pandas as pd 
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

"""csv読みこみ"""
path1="customer_join.csv"
customer=pd.read_csv(path1)
customer_clustering=customer[["mean","median","max","min","membership_period"]]

"""データフレームをkmeansで計算できるように、標準化"""
sc=StandardScaler()
customer_clustering_sc=sc.fit_transform(customer_clustering)#標準化

"""kmeans法"""
kmeans=KMeans(n_clusters=4,random_state=0)#クラスター数を決める
clusters=kmeans.fit(customer_clustering_sc)#kmeansに標準化された配列を代入
customer_clustering["cluster"]=clusters.labels_#クラスターラベルを取得


"""結果分析"""

customer_clustering.columns=["月内平均","月内中央値","月内最大値","月内最小値","会員期間","cluster"]

print(customer_clustering.groupby("cluster").count())#各クラスタごにindexが保存されている:.group()で中身みれる
print(customer_clustering.groupby("cluster").mean())