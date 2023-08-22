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



