import pickle
import numpy as np
import streamlit as st
import os
import string
model = pickle.load(open('pickled_Gbr.pkl', 'rb'))

def main():
    st.title('Primary Education Completion Rate')
    
    #input variables
    Childhood_Education_GER = st.text_input('Childhood Education GER')
    Gross_enrolment_ratio_early_childhood_educational_development_programmes = st.text_input('GER early childhood educational development programmes')
    Gross_intake_ratio_to_the_last_grade_of_primary_education = st.text_input('Gross intake ratio to the last grade of primary education')
    Literacy_rate_for_25_64_years_old  = st.text_input('Literacy rate for 25-64 years old')
    Expenditure_on_education_as_a_percentage_of_total_government_expenditure = st.text_input('Expenditure on education as a percentage of total government expenditure')
    Government_expenditure_on_education_as_a_percentage_of_GDP = st.text_input('Government expenditure on education as a percentage of GDP')
    Central_Asia = st.text_input('Central Asia')
    Central_and_Southern_Asia = st.text_input('Central and Southern Asia')
    Eastern_and_South_Eastern_Asia = st.text_input('Eastern and South-Eastern Asia')
    Europe_and_Northern_America = st.text_input('Europe and Northern America')
    Latin_America_and_the_Caribbean = st.text_input('Latin America and the Caribbean')
    Northern_Africa_and_Western_Asia = st.text_input('Northern Africa and Western Asia')
    Oceania = st.text_input('Oceania')
    Gender_numerical = st.text_input('Gender_numerical')
    makeprediction = ""
    
#prediction code
    if st.button('Predict'):
        makeprediction = model.predict([[Childhood_Education_GER, Gross_enrolment_ratio_early_childhood_educational_development_programmes, Gross_intake_ratio_to_the_last_grade_of_primary_education,
                                         Literacy_rate_for_25_64_years_old, Expenditure_on_education_as_a_percentage_of_total_government_expenditure, Government_expenditure_on_education_as_a_percentage_of_GDP,
                                         Central_Asia, Central_and_Southern_Asia, Eastern_and_South_Eastern_Asia,
                                         Europe_and_Northern_America, Latin_America_and_the_Caribbean, Northern_Africa_and_Western_Asia, Oceania, Gender_numerical]])
        output = round(makeprediction[0],2)
        st.success('Primary School Completion Rate {}'.format(output))
    
if __name__=="__main__":
    main()
