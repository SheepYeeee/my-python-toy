import numpy as np
import pandas as pd 
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC

raw_iris=datasets.load_iris()
print(raw_iris.keys())
print(raw_iris['data'])#feature值
print(raw_iris['target'])#目標值
print(raw_iris['target_names'])#目標標籤
print(raw_iris['DESCR'])#資料集內容描述
print(raw_iris['feature_names'])#屬性名稱
print(np.unique(raw_iris['target']))#類別種類


df_x=pd.DataFrame(raw_iris['data'])
df_y=pd.DataFrame(raw_iris['target'])
x_train,x_test,y_train,y_test=train_test_split(df_x, df_y, test_size=0.3)

lin_clf=LinearSVC()#初始化LinearSVC
lin_clf.fit(x_train,y_train.values.ravel())
#使用 fit 來建置模型，其參數接收 training data matrix, testing data array，所以進行 y_train.values.ravel() Data Frame 轉換

knn=KNeighborsClassifier()#初始化KNeighborsClassifier
knn.fit(x_train,y_train.values.ravel())
#使用 fit 來建置模型，其參數接收 training data matrix, testing data array，所以進行 y_train.values.ravel() 轉換

print(lin_clf.predict(x_test))#使用x_test來預測結果
print(lin_clf.score(x_test,y_test))#印出預測準確率

print(knn.predict(x_test))#使用x_test來預測結果
print(knn.predict_proba(x_test))#印出testing data預測標籤機率
print(knn.score(x_test,y_test))#印出預測準確
