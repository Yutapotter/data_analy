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

#クラスタリング結果の可視化

from sklearn.decomposition import PCA
X=customer_clustering_sc
pca=PCA(n_components=2)#次元圧縮のインスタンスを作成

x_pca=pca.fit_transform(X)#fitで主成分分析,transformで元データを主成分に変換
pca_df=pd.DataFrame(x_pca)#データフレームに変換


pca_df["cluster"]=customer_clustering["cluster"]

import matplotlib.pyplot as plt 
for i in customer_clustering["cluster"].unique():
    tmp=pca_df.loc[pca_df["cluster"]==i]
    plt.scatter(tmp[0],tmp[1])