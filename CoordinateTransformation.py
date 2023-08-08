import pickle
import numpy as np
import os
from db import ReadData,AddData
from sklearn.decomposition import PCA #主成分分析器
import matplotlib.pyplot as plt

# データをロード&次元圧縮&アップロード
def main():#独立して実行
    if os.path.exists("cache/data.pkl"):
        with open("cache/data.pkl","rb") as f:
            L=pickle.load(f)
    else:
        L=ReadData()
        L=[l.to_dict() for l in L]
        with open("cache/data.pkl","wb") as f:
            pickle.dump(L,f)
    
    A=np.array([l["embedding"] for l in L])

    pca = PCA(n_components=3)
    pca.fit(A)
    print(A.shape)
    # データを主成分空間に写像
    feature = pca.transform(A)

    # さらに極座標(r,theta,phi)に変換
    r = np.sqrt(feature[:,0]**2+feature[:,1]**2+feature[:,2]**2)
    theta = np.arccos(feature[:,2]/r)
    phi = np.arctan2(feature[:,1],feature[:,0])

    print(r.shape,theta.shape,phi.shape)
    print(np.max(r),np.min(r))
    print(np.max(theta),np.min(theta))
    print(np.max(phi),np.min(phi))

    for i in range(r.shape[0]):
        L[i]["polar_cord"]=[r[i],theta[i],phi[i]]
        # AddData(L[i]["channel_id"],L[i])

        # print(r[i],theta[i],phi[i])

if __name__ == "__main__":
    main()