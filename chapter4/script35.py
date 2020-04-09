import pandas as pd 
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

#csvファイルの読み込み

customer=pd.read_csv("customer_join.csv")
customer_clustering=customer[["mean","median","max","min","membership_period"]]

#クラスタリング

sc=StandardScaler()
customer_clustering_sc=sc.fit_transform(customer_clustering)

kmeans=KMeans(n_clusters=4,random_state=0)
clusters=kmeans.fit(customer_clustering_sc)
customer_clustering["cluster"]=clusters.labels_

customer_clustering.columns=["月内平均","月内中央値","月内最大値","月内最小値","会員期間","cluster"]

#主成分分析

from sklearn.decomposition import PCA
X=customer_clustering
pca=PCA(n_components=2)
x_pca=pca.fit_transform(X)
pca_df=pd.DataFrame(x_pca)
pca_df["cluster"]=customer_clustering["cluster"]


#退会顧客の傾向を把握

customer_clustering=pd.concat([customer_clustering,customer],axis=1)
print(customer_clustering.groupby(["cluster","is_deleted"],as_index=False).count()[["cluster","is_deleted","customer_id"]])


print(customer_clustering.groupby(["cluster","routine_flg"],as_index=False).count()[["cluster","routine_flg","customer_id"]])