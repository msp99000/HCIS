import sqlite3
import pandas as pd
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_option_menu import option_menu
from styles import streamlit_style

streamlit_style()

# Connect to the SQLite database
conn = sqlite3.connect('hcis.db')
cursor = conn.cursor()

# Horizontal Menu
selected = option_menu(None, ["Home", "Patients", "Admissions", 'Dashboard'], 
    icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=3, orientation="horizontal")
if selected == 'Home':
    switch_page('Home')
if selected == 'Patients':
    switch_page('Patients')
if selected == 'Admissions':
    switch_page('Admissions')

state = st.session_state

st.header('Patient Dashboard')

state.subject_id = st.text_input("Enter the Patient ID")

def dashboard(id):
    cursor.execute(f'''
                        SELECT
                            p.subject_id AS "Patient ID",
                            p.lang AS "Language",
                            p.religion AS "Religion",
                            p.marital_status AS "Marital Status",
                            p.ethnicity AS "Ethnicity",
                            a.admittime AS "Admission Time",
                            a.diagnosis AS "Diagnosis",
                            d.short_title AS "Procedure",
                            pr.startdate AS "Prescription Start Date",
                            pr.enddate AS "Prescription End Date",
                            pr.drug AS "Prescribed Drug"
                        FROM
                            PATIENTS p
                            LEFT JOIN ADMISSIONS a ON p.subject_id = a.subject_id
                            LEFT JOIN DIAGNOSIS d ON a.hadm_id = d.hadm_id
                            LEFT JOIN PRESCRIPTIONS pr ON a.hadm_id = pr.hadm_id
                        WHERE
                            p.subject_id = {id}
                ''')

    res = cursor.fetchall()
    df = pd.DataFrame(res, columns=["Patient ID", "Language", "Religion", "Marital Status", "Ethnicity", "Admission Time", "Diagnosis", "Procedure", "Prescription Start Date", "Prescription End Date", "Drug"])
    st.dataframe(df)

if st.button('Show Dashboard'):
    dashboard(state.subject_id)
