#Importing libraries
import numpy as np
import pandas as pd
import sklearn as sk
import seaborn as sn
import matplotlib.pyplot as plt
df=pd.read_csv("/Users/abhijeetgupta/Downloads/Student_performance.csv")
df=df.drop("nombre",axis="columns")
df=df.drop("sexo",axis="columns")
df=df.drop("id_Alumno",axis="columns")
df=df.drop("Intra_Final",axis="columns")
df=df.drop("Inter_Final",axis="columns")
df=df.drop("Adap_Final",axis="columns")
df=df.drop("Impre_Final",axis="columns")
for i in range(0,len(df.grado)):
    df.grado[i]=df.grado[i][0]
df['grado'] = df['grado'].astype(int)
df["rendi_academico"] = pd.factorize(df["rendi_academico"])[0]
df.P15[232]=2
inputs=df.drop("rendi_academico",axis="columns")
output=df.rendi_academico
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(inputs,output,test_size=0.2,stratify=df[["rendi_academico"]],random_state=1) 
from sklearn import ensemble
model=ensemble.RandomForestClassifier(n_estimators=100,random_state=8)
model.fit(X_train,Y_train)
Y_predict = model.predict(X_test)
print(Y_predict)
from sklearn import metrics
import pickle
#from sklearn.externals import joblib
import joblib
filename="student_performance.pkl"
pickle.dump(model, open(filename,'wb'))