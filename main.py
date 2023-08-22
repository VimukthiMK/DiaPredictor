#import Streamlit
import streamlit as st

#import libraries
import numpy as np
import pandas as pd

# import scikit -learn
#perform Scaling
from sklearn.preprocessing import StandardScaler 
#train test split
from sklearn.model_selection import train_test_split 
#SVM ML model
from sklearn import svm 
#Check prediction Accuraccy
from sklearn.metrics import accuracy_score 

#import diabetes.csv
df=pd.read_csv('./data/diabetes.csv')

# Headings of app
st.title('DiaPredictor -Live Diabetes Checker')

#Visualize Training Data Description
st.subheader('Training Data Stats')
st.write(df.describe())


# SideBar
st.sidebar.header('Patient Data')
st.sidebar.write('Please Adjust Your Values')

# Sidebar Function
def user_report():
  pregnancies = st.sidebar.slider('Pregnancies', 0,20, 3 )
  glucose = st.sidebar.slider('Glucose (mg/dL)', 0,250, 120 )
  bp = st.sidebar.slider('Blood Pressure (mm Hg)', 0,180, 70 )
  skinthickness = st.sidebar.slider('Skin Thickness (mm)', 0,100, 20 )
  insulin = st.sidebar.slider('Insulin (μU/mL)', 0,1000, 79 )
  bmi = st.sidebar.slider('BMI (kg/m²)', 0,67, 20 )
  dpf = st.sidebar.slider('Diabetes Pedigree Function', 0.0,2.5, 0.47 )
  age = st.sidebar.slider('Age', 1,100, 33 )

  user_report_data = {
      'Pregnancies':pregnancies,
      'Glucose':glucose,
      'BP':bp,
      'Skin Thickness':skinthickness, 
      'Insulin':insulin,
      'BMI':bmi,
      'DPF':dpf,
      'Age':age
  }

#Insert Navbar data to a Dataframe
  report_data = pd.DataFrame(user_report_data, index=[0])
  return report_data


# Patient data
user_data = user_report()
st.subheader('Patient Data')
st.write(user_data)

#Seperate Outcome column and make X,Y
X= df.drop(columns='Outcome', axis=1)
Y=df['Outcome']

#Standard Scalar
scaler = StandardScaler()
#fit on X
scaler.fit(X)

#Store Standardized X data
standard_data = scaler.transform(X)

#Load standadized data back to X
X = standard_data
# split data
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2)

#Classification-vector classifier
clf=svm.SVC(kernel='linear')

#Train dataset
clf.fit(X_train,Y_train)

#Insert navbar data into numpy array
input_sample = np.array(user_data)

#Reshape the array
input_npArray_reshaped = input_sample.reshape(1, -1)
#Store Standardized sample data
std_data = scaler.transform(input_npArray_reshaped)

# OUTPUT
predict = clf.predict(std_data)
st.subheader('Your Diabetic Report: ')
output=''
if predict[0]==0:
  output = 'Congrats !! You are not Diabetic 😇'
else:
  output = 'Sorry...You are Diabetic 😔'
st.title(output)

#Measure accuracy of Report
st.subheader('Accuracy: ')
st.write(str(accuracy_score(Y_test, clf.predict(X_test))*100)+'%')




