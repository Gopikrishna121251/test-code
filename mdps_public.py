import pickle
import streamlit as st
import base64

# Loading the saved models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
#heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
#parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))
#breast_cancer_prediction = pickle.load(open('breast_cancer_data.sav','rb'))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                           # 'Heart Disease Prediction',
                           # 'Parkinsons Prediction',
                            #'Breast Cancer Prediction'],
                           #icons=['activity','heart','person','building add'],
                           default_index=0)

# Function to get the base64 encoding of a binary file
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Function to set PNG image as page background
def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Set background image
set_png_as_page_bg('background.png')

# Show different pages based on selection
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    
    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        SkinThickness = st.text_input('Skin Thickness value')
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Glucose = st.text_input('Glucose Level')
        Insulin = st.text_input('Insulin Level')
        Age = st.text_input('Age of the Person')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
        BMI = st.text_input('BMI value')

    # Code for Prediction
    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
            st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcmRvZWNydGhtdnV4anJnZmE0eDB4YmtwY3Z4c2ltOG8za2oxeTh1NSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/mlvseq9yvZhba/giphy.gif")
        else:
            diab_diagnosis = 'The person is not diabetic'
    st.success(diab_diagnosis)
