import streamlit as st
import pickle 
import math as mt
import os
import numpy as np

target = 'C:/Users/clinton/Downloads/ds_projects/hamoye_intern/model_building/prri_data.pkl'
primary_data = pickle.load(open('primary_dataa.pkl', 'rb'))
upper_secondary_data = pickle.load(open('Upper_secondary_model.pkl', 'rb'))
lower_secondary_data = pickle.load(open('Lower_secondary_model.pkl', 'rb'))
    

# # primary_model = pc.load(open('primary_model.sav', 'rb'))
# # lower_secondary_model = pc.load(open('Lower_secondary_model.sav', 'rb'))
# # upper_secondary_model = pc.load(open('Upper_secondary_level.sav', 'rb'))


def primary_model(input_data):
    input_data_to_numpy = np.asarray(input_data)
    input_data_reshaped = input_data_to_numpy.reshape(1, -1)
    prediction = primary_data.predict(input_data_reshaped)
    return mt.ceil(prediction) * 100
    
def upper_secondary_model(input_data):
    input_data_to_array = np.asanyarray(input_data)
    reshaped_input = input_data_to_array.reshape(1, -1)
    prediction = upper_secondary_data.predict(reshaped_input)
    return mt.ceil(prediction) * 100
    
def lower_secondary_model(input_data):
    input_data_to_array = np.asanyarray(input_data)
    reshaped_input = input_data_to_array.reshape(1, -1)
    prediction = lower_secondary_data.predict(reshaped_input)
    return mt.ceil(prediction) * 100 
    

def main():

    st.title('Predicting school completion in different sub levels in school')

    result = st.selectbox(label='select school level', options=('Primary school', 
                                        'Lower secondary level', 'Upper secondary level'))


    st.write('You selected :', result)

    
    completion_prediction = ''
    lower_completion_prediction = ''
    upper_completion_prediction = ''
    
    if result == 'Primary school':
        Year = st.text_input('Year')
        Childhood_Education_GER = st.text_input('Childhood Education GER')
        early_childhood_educational_development_programmes = st.text_input('early childhood educational development programmes')
        Gross_intake_ratio = st.text_input('Gross intake ratio to the last grade of primary education')
        Literacy_rate_for_25_64_years_old = st.text_input('Literacy rate for 25-64 years old')
        Government_expenditure_on_education_as_a_percentage_of_GDP = st.text_input('Government expenditure on education as a percentage of GDP (%)')
        Central_Asia = st.text_input('Central Asia')
        Central_and_Southern_Asia = st.text_input('Central and Southern Asia')
        Eastern_and_South_Eastern_Asia = st.text_input('Eastern and South-Eastern Asia')
        Europe_and_Northern_America = st.text_input('Europe and Northern America')
        Latin_America_and_the_Caribbean = st.text_input('Latin America and the Caribbean')
        Northern_Africa_and_Western_Asia = st.text_input('Northern Africa and Western Asia')
        Oceania = st.text_input('Oceania')
        Gender_numerical = st.text_input('Gender numerical')

        if st.button('Prediction button'):
            completion_prediction = primary_model([Year, Childhood_Education_GER,
                                                 early_childhood_educational_development_programmes,
                                                 Gross_intake_ratio,
                                                 Literacy_rate_for_25_64_years_old,
                                                 Government_expenditure_on_education_as_a_percentage_of_GDP,
                                                 Central_Asia, Central_and_Southern_Asia,
                                                 Eastern_and_South_Eastern_Asia, 
                                                 Europe_and_Northern_America,
                                                 Latin_America_and_the_Caribbean,
                                                 Northern_Africa_and_Western_Asia,
                                                 Oceania,
                                                 Gender_numerical
                                                 ])
            
        st.success(completion_prediction)
        
    elif result == 'Upper secondary level':
        Year = st.text_input('Year')
        Gross_enrollment_ratio = st.text_input('Gross enrollment') 
        Childhood_Education_GER = st.text_input('Childhood Education GER')
        early_childhood_educational_development_programmes = st.text_input('early childhood educational development programmes')
        Gross_intake_ratio = st.text_input('Gross intake ratio to the last grade of primary education')
        Literacy_rate_for_25_64_years_old = st.text_input('Literacy rate for 25-64 years old')
        Government_expenditure_on_education_as_a_percentage_of_GDP = st.text_input('Government expenditure on education as a percentage of GDP (%)')
        Central_Asia = st.text_input('Central Asia')
        Central_and_Southern_Asia = st.text_input('Central and Southern Asia')
        Eastern_and_South_Eastern_Asia = st.text_input('Eastern and South-Eastern Asia')
        Europe_and_Northern_America = st.text_input('Europe and Northern America')
        Latin_America_and_the_Caribbean = st.text_input('Latin America and the Caribbean')
        Northern_Africa_and_Western_Asia = st.text_input('Northern Africa and Western Asia')
        Oceania = st.text_input('Oceania')
        Gender_numerical = st.text_input('Gender numerical')

        if st.button('Prediction button'):
            upper_completion_prediction = upper_secondary_model([Year, Gross_enrollment_ratio,
                                                                 Childhood_Education_GER,
                                            early_childhood_educational_development_programmes,
                                            Gross_intake_ratio,
                                            Literacy_rate_for_25_64_years_old,
                                            Government_expenditure_on_education_as_a_percentage_of_GDP,
                                            Central_Asia, Central_and_Southern_Asia,
                                            Eastern_and_South_Eastern_Asia, 
                                            Europe_and_Northern_America,
                                            Latin_America_and_the_Caribbean,
                                            Northern_Africa_and_Western_Asia,
                                            Oceania,
                                            Gender_numerical])
        st.success(upper_completion_prediction)

    elif result == 'Lower secondary level':
        Year = st.text_input('Year')
        Gross_enrollment_ratio = st.text_input('Gross enrollment') 
        Childhood_Education_GER = st.text_input('Childhood Education GER')
        early_childhood_educational_development_programmes = st.text_input('early childhood educational development programmes')
        Gross_intake_ratio = st.text_input('Gross intake ratio to the last grade of primary education')
        Literacy_rate_for_25_64_years_old = st.text_input('Literacy rate for 25-64 years old')
        Government_expenditure_on_education_as_a_percentage_of_GDP = st.text_input('Government expenditure on education as a percentage of GDP (%)')
        Central_Asia = st.text_input('Central Asia')
        Central_and_Southern_Asia = st.text_input('Central and Southern Asia')
        Eastern_and_South_Eastern_Asia = st.text_input('Eastern and South-Eastern Asia')
        Europe_and_Northern_America = st.text_input('Europe and Northern America')
        Latin_America_and_the_Caribbean = st.text_input('Latin America and the Caribbean')
        Northern_Africa_and_Western_Asia = st.text_input('Northern Africa and Western Asia')
        Oceania = st.text_input('Oceania')
        Gender_numerical = st.text_input('Gender numerical')

        if st.button('Prediction button'):
            lower_completion_prediction = upper_secondary_model([Year, Gross_enrollment_ratio,
                                                                 Childhood_Education_GER,
                                            early_childhood_educational_development_programmes,
                                            Gross_intake_ratio,
                                            Literacy_rate_for_25_64_years_old,
                                            Government_expenditure_on_education_as_a_percentage_of_GDP,
                                            Central_Asia, Central_and_Southern_Asia,
                                            Eastern_and_South_Eastern_Asia, 
                                            Europe_and_Northern_America,
                                            Latin_America_and_the_Caribbean,
                                            Northern_Africa_and_Western_Asia,
                                            Oceania,
                                            Gender_numerical])
        st.success(lower_completion_prediction)






if __name__ == '__main__':
    main() 

