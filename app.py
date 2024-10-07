
import joblib
import streamlit as st
from PIL import Image

load_model = joblib.load('Heart Disease Pred Model')

def prediction(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal) :
    
    if sex == 'Male': 
        sex = 1
    elif sex == 'Female':
        sex = 0
        
    if cp == 'Typical angina':
        cp = 0
    elif cp == 'Atypical angina':
        cp = 1
    elif cp == 'Non-anginal pain':
        cp = 2
    elif cp == 'Asymptomatic':
        cp = 3
    
    if fbs == 'Greater than 120 mg/dl':
        fbs = 1
    elif fbs == 'Less than 120 mg/dl' : 
        fbs = 0
        
    if restecg == 'Normal':
        restecg = 0
    elif restecg == 'Abnormality related to ST-T wave':
        restecg = 1
    elif restecg == "Showing probable or definite left ventricular hypertrophy by Estes' criteria":
        restecg = 2
        
    if exang == 'Yes':
        exang = 1
    elif exang == 'No':
        exang = 0
        
    if slope == 'Upsloping':
        slope = 0
    elif slope == 'Flat':
        slope = 1
    elif slope =='Downsloping':
        slope  = 2
        
    if thal == 'Normal':
        thal = 1
    elif thal == 'Fixed defect':
        thal = 2
    elif thal == 'Reversible defect':
        thal = 3
        
    prediction_result = load_model.predict([[age, sex, cp, trestbps, chol, 
                                           fbs, restecg, thalach, exang, 
                                           oldpeak, slope, ca, thal]])
    
    if (prediction_result == 1) :
        msg = "Based on the data provided, model suggests potential presence of Heart Disease"
    
    else :
        msg = "Based on the data provided, model indicates no presence of Heart Disease"
    
    return msg
        
    
def main():       
   
    im = Image.open('icon_image.png')
    
    st.set_page_config(layout = 'wide',page_title="Heart Health Predictive ML App", page_icon = im)
    
    html_temp = """ 
    <div style ="background-color:Gray; padding : 13px"> 
    <h1 style ="color:black; text-align:center;">Heart Health Predictive ML App</h1> 
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True) 
    
    try :
        
        c1,c2,c3 = st.columns(3)
        
        with c1:
            age = st.text_input('Age')
            sex = st.selectbox('Gender',("Male","Female"))
            cp = st.selectbox('Chest pain type',("Typical angina","Atypical angina","Non-anginal pain","Asymptomatic")) 
            trestbps = st.text_input('Resting blood pressure (mm Hg)')
            chol = st.text_input('Serum cholestrol (mg/dl)')
            
        with c2:
            fbs = st.selectbox('Fasting blood sugar',("Greater than 120 mg/dl","Less than 120 mg/dl"))
            restecg = st.selectbox('Resting electrocardiographic measurement',("Normal","Abnormality related to ST-T wave",
                               "Showing probable or definite left ventricular hypertrophy by Estes' criteria"))
            thalach = st.text_input('Maximum heart rate achieved')
            
            exang = st.selectbox('Exercise induced angina',("Yes","No"))
            oldpeak = age = st.text_input('ST depression induced by exercise relative to rest')
            
        with c3:    
            slope = st.selectbox('Slope of the peak exercise ST segment',("Upsloping","Flat","Downsloping"))
            ca = st.text_input('Number of major vessels (0-3) colored by flouroscopy')
            thal = st.selectbox('Type of thalassemia',("Normal","Fixed defect","Reversible defect"))
    
        result =""
       
        if st.button("Result"): 
            result = prediction(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal) 
            st.success(result)
            
    except ValueError :
        st.error("Enter valid data")
            

if __name__=='__main__': 
    main()
