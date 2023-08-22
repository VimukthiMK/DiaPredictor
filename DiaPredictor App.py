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