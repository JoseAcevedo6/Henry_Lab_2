from sklearn.tree import DecisionTreeClassifier
from pandas import DataFrame, read_csv

from transform import transform


data = read_csv('./datasets/hospitalizaciones_train.csv')

le = [
        'Department', 'Ward_Facility_Code', 'doctor_name', 'Age', 'gender',
        'Type of Admission', 'Severity of Illness', 'health_conditions', 'Insurance']

ss = ['Available Extra Rooms in Hospital', 'staff_available', 'Visitors with Patient', 'Admission_Deposit']

target = ['Stay (in days)']

X_Train, X_Test, Y_Train, Y_Test = transform(
        data, to_le=le, to_ss=ss, to_tts=target, ros=False, test_size=0.2, random_state=42, array=False)

dtc_model = DecisionTreeClassifier(max_depth=13, criterion='entropy', random_state=42)
dtc_model.fit(X_Train, Y_Train)
Y_Pred = dtc_model.predict(X_Test)


data2 = read_csv('./datasets/hospitalizaciones_test.csv')

eval = transform(data2, to_le=le, to_ss=ss)

predition = DataFrame(dtc_model.predict(eval), columns=['pred'])
predition.to_csv('JoseAcevedo6', index=False)
