# Diabetes Checker

This project is a simple web application built using Streamlit and scikit-learn that predicts whether a person is diabetic or not based on their health metrics. It uses a Support Vector Machine (SVM) classifier for prediction and provides an interface for users to input their health data and receive predictions.

## Getting Started

To run the Diabetes Checker app on your local machine, follow these steps:

1. Clone the repository to your local machine:
   ```sh
   git clone https://github.com/VimukthiMK/DiaPredictor.git
2. Navigate to the project directory:
   ```sh
   cd DiaPredictor
3. Install the required dependencies. It's recommended to set up a virtual environment before installing the dependencies:
   ```sh
   pip install -r requirements.txt

4. Run the Streamlit app:
   ```sh
   streamlit run main.py

## Project Structure

The project is organized as follows:
<ul>
  <li>app.py           : Main Streamlit application file with user interface and prediction logic.</li>
  <li>diabetes.csv     : Dataset used for training and testing the SVM model.</li>
  <li>README.md        : Project information and setup instructions.</li>
  <li>requirements.txt : List of required Python packages.</li>
</ul>
   
    
## How the App Works

The app provides an interface where users can adjust their health metrics using sliders on the sidebar. These metrics include pregnancies, glucose level, blood pressure, skin thickness, insulin level, BMI, diabetes pedigree function, and age. The app then uses a trained SVM classifier to predict whether the user is diabetic or not based on the provided metrics. The accuracy of the model is also displayed on the interface.

## Technologies Used

 <ul>
   <li> Streamlit: Python library for creating web applications.</li>
    <li>scikit-learn: Machine learning library for training SVM models.</li>
 </ul>

## Acknowledgments
Dataset sourced from the <b>Pima Indians Diabetes Database.</b>
