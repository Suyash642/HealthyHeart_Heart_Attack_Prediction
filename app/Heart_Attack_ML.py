#importing libraries
import pandas as pd
import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from scipy import stats
import pickle

df = pd.read_csv('D:\\ML WEB Projects\\djangoproject\\mljango\\app\\heart_attack.csv')

z = np.abs(stats.zscore(df))
df_outliers= df[(z >= 3.5).any(axis=1)] 
df_clean=df[(z <3.5).all(axis=1)]

data = pd.get_dummies(df_clean,columns =['cp','restecg','slope','ca','thal'])
numeric_cols=['age','trestbps','chol','thalach','oldpeak']
standardScaler = StandardScaler()
data[numeric_cols] = standardScaler.fit_transform(data[numeric_cols])

y=data['target']
y=np.array(y)
x=data.drop(columns=['target'])

from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import ExtraTreesClassifier

clf = ExtraTreesClassifier(n_estimators=500).fit(x, y)
selector = SelectFromModel(clf, prefit=True)

x_columns=x.columns 
columns=selector.get_support()
selected_columns=list([x_columns[i] for i in range(len(columns)) if columns[i]==True]) 

x_reduced=selector.transform(x)

x_train, x_test, y_train, y_test = train_test_split(x_reduced, y, test_size=0.30,  random_state=42)

svm_model = svm.SVC(kernel='linear') 
svm_model.fit(x_train,y_train)
y_predict4 = svm_model.predict(x_test)

"""
    Selected Important Features are: ['age', 'trestbps', 'chol', 'thalach', 'exang', 'oldpeak', 'cp_0', 'slope_2',
                                      'ca_0', 'thal_2', 'thal_3']

    SVM Model Accuracy score: 86.0%
    SVM f1 score: 0.8737864077669903

    Confusion Matrix for SVM
    [[32  6]
    [ 7 45]]


    Predicted   0   1  All
    Actual                
    0          32   6   38
    1           7  45   52
    All        39  51   90

    Classification Report
                precision    recall  f1-score   support

            0       0.82      0.84      0.83        38
            1       0.88      0.87      0.87        52

        accuracy                           0.86        90
        macro avg       0.85      0.85      0.85        90
        weighted avg       0.86      0.86      0.86        90

"""
pickle.dump(svm_model, open('svmmodel.pkl', 'wb'))