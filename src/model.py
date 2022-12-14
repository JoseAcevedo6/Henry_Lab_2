from sklearn.neighbors import KNeighborsClassifier
from pandas import DataFrame, read_csv

from etl import transform


data = read_csv('./datasets/hospitalizaciones_train.csv')
columns = ['Department', 'Ward_Facility_Code', 'doctor_name', 'Age', 'gender', 'Stay (in days)']
X_Train, X_Test, Y_Train, Y_Test = transform(
        data, columns, target='Stay (in days)', test_size=0.20, random_state=42, array=True, scalar=True)

knn_model = KNeighborsClassifier(n_neighbors=7)
knn_model.fit(X_Train, Y_Train)
Y_Pred = knn_model.predict(X_Test)

data2 = read_csv('./datasets/hospitalizaciones_test.csv')
columns_data2 = ['Department', 'Ward_Facility_Code', 'doctor_name', 'Age', 'gender']
eval = transform(data2, columns_data2, array=True, scalar=True)

predition = DataFrame(knn_model.predict(eval))
predition.columns = ['pred']
predition.to_csv('JoseAcevedo6', index=False)
