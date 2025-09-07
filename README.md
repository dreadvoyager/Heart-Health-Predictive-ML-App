# Heart Health Predictive ML App

## Table of Contents
- [Introduction](#introduction)  
- [Problem Statement](#problem-statement)  
- [Objectives](#objectives)  
- [Dataset](#dataset)  
- [Methodology](#methodology)  
- [Models Used](#models-used)  
- [Evaluation Metrics](#evaluation-metrics)  
- [Results](#results)  
- [Deployment](#deployment)  
- [Tools and Technologies](#tools-and-technologies)  
- [Future Work](#future-work)  
- [Usage](#usage)  

## Introduction
Heart disease is a leading cause of death globally. Early detection is critical for effective treatment. This project leverages machine learning to predict the likelihood of heart disease using patient health metrics.  

## Problem Statement
Develop a machine learning model to predict heart disease based on patient attributes such as age, blood pressure, cholesterol, and exercise levels, providing healthcare professionals with a reliable diagnostic tool.  

## Objectives
- Build a predictive model for heart disease detection.  
- Compare various machine learning algorithms to identify the best-performing model.  
- Deploy the final model with a user-friendly interface for real-time predictions.  

## Dataset
- Contains patient records with attributes including age, sex, chest pain type, resting blood pressure, cholesterol, fasting blood sugar, etc.  
- Target variable: `0` = No Heart Disease, `1` = Presence of Heart Disease.  

## Methodology
1. **Data Preprocessing:** Handled missing values, normalized features using StandardScaler.  
2. **Exploratory Data Analysis:** Visualized feature distributions and correlations.  
3. **Model Training:** Trained multiple models including KNN, Logistic Regression, Decision Tree, Random Forest, and Gradient Boosting.  
4. **Model Evaluation:** Evaluated models using accuracy, precision, recall, and F1-score.  
5. **Model Selection:** Chose Random Forest as the best-performing model with 87% accuracy.  
6. **Deployment:** Developed a Streamlit web application for real-time predictions.  

## Models Used
- K-Nearest Neighbors (KNN)  
- Logistic Regression  
- Decision Tree Classifier  
- Random Forest Classifier  
- Gradient Boosting Classifier  

## Evaluation Metrics
- **Accuracy:** 94% (Random Forest)  
- **Precision, Recall, F1-score:** Balanced for both classes  

## Results
Random Forest was selected as the final model due to its superior performance across all evaluation metrics. Visualizations such as confusion matrices and accuracy comparisons were generated to support model selection.  

## Deployment
The final model has been deployed using **Streamlit**, allowing users to input patient data through an interactive web interface and receive instant predictions on heart disease presence.  

## Tools and Technologies
- **Languages & Libraries:** Python, NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn  
- **Web Deployment:** Streamlit  
- **Development Environment:** Jupyter Notebook  

## Future Work
- Incorporate additional features and external datasets for improved predictions.  
- Explore ensemble learning techniques like stacking and boosting.  
- Implement model interpretability using SHAP or LIME.  
- Deploy in clinical settings for real-world validation.  

## Usage
1. Clone the repository:  
```bash
git clone <repository_url>
```
2. Install required packages:  
```bash
pip install -r requirements.txt
```
3. Run the Streamlit app:
```bash
streamlit run app.py
```
4. Input patient data to receive real-time predictions.
