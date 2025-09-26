## Importing the libraries
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import pickle

# Loading the model
loaded_model = pickle.load(open('loan_classifier', 'rb'))

# Importing the dataset
load = pd.read_csv('diabetes.csv')

# Functions for the loan prediction
def loan_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)
    return 'Unfortunately, you are susceptible to diabetes.' if prediction[0] == 0 else 'Congratulations! You are not susceptible to diabetes.'

    #Creating a count plot for gender
def chart_page():
    st.title('Loan Application by Gender')
    count_gender=px.histogram(
        load,
        x = 'Gender',
        color='Loan_Status',
        title='Gender Status of Loan Applicants',
        labels={'Loan_Status': 'Loan_Status'})
    st.plotly_chart(count_gender)    ## To show the plot

    # Adding some insights
    st.subheader('Insights')
    st.markdown('Men apply for ;oan more than women')

def dashboard_page():
    st.title('Dashboard Page')
    st.markdown('Input your values')

    # Collecting the user inputs
    col1, col2, col3 = st.columns(3)  ## To specify the number of columns
    
    with col1:
        Pregnancies= st.number_input('Pregnancies', value = 0)
        Glucose= st.number_input('Glucose', value = 0)
        BloodPressure= st.number_input('BloodPressure', value = 0)
        SkinThickness= st.number_input('SkinThickness', value = 0)

    with col2:
        Insulin= st.number_input('Insulin', value = 0)
        BMI= st.number_input('LoanAmount', value = 0)
        Age= st.number_input('LoanAmount', value = 0)
        Age= st.number_input('LoanAmount', value = 0)

    if st.button('Diabetes Prediction System'):
        try:
            input_data = [
                int(Pregnancies),
                int(Glucose),
                int(BloodPressure),
                int(SkinThickness),
                int(Insulin),
                float(BMI),
                float(DiabetesPedigreeFunction),
                int(Age)
        ]
            result = diabetes_prediction(input_data)
            st.success(result)
        except ValueError:
            st.error('Enter a valid input')

            # Function to switch tabs
def main():
    st.sidebar.title('Navigation')
    page = st.sidebar.selectbox('Select Page', ['Chart', 'Form Inputs'])

    if page == 'Chart':
        chart_page()
    elif page=='Form Inputs':
        dashboard_page()

# Run app
if __name__ == '__main__':
    main()

