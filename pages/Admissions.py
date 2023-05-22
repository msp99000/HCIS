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
    menu_icon="cast", default_index=2, orientation="horizontal")
if selected == 'Home':
    switch_page('Home')
if selected == 'Patients':
    switch_page('Patients')
if selected == 'Dashboard':
    switch_page('Dashboard')

state = st.session_state

st.header('Admissions')
menu_options = ["View Admissions", "Create New Admission"]
selected_option = st.selectbox("Select Options", menu_options)

def view_admissions():
    st.subheader("View Admissions")
    cursor.execute("SELECT * FROM ADMISSIONS")
    admissions = cursor.fetchall()
    df = pd.DataFrame(admissions, columns=["HADM ID", "Subject ID", "Admittime", "Dischtime", "Deathtime",
                                           "Admission Type", "Admission Location", "Discharge Location",
                                           "ED Regtime", "ED Outtime", "Diagnosis", "Hospital Expire Flag",
                                           "Has Chartevents Data"])
    st.dataframe(df)


def create_admission():
    st.subheader("Create New Admission")
    hadm_id = st.number_input("HADM ID", min_value=0, step=1)
    subject_id = st.number_input("Subject ID", min_value=0, step=1)
    admittime = st.text_input("Admission Time")
    dischtime = st.text_input("Discharge Time")
    deathtime = st.text_input("Death Time")
    admission_type = st.text_input("Admission Type")
    admission_location = st.text_input("Admission Location")
    discharge_location = st.text_input("Discharge Location")
    edregtime = st.text_input("ED Registration Time")
    edouttime = st.text_input("ED Out Time")
    diagnosis = st.text_input("Diagnosis")
    hospital_expire_flag = st.checkbox("Hospital Expire Flag")
    has_chartevents_data = st.checkbox("Has Chartevents Data")

    if st.button("Save"):
        cursor.execute("""
            INSERT INTO ADMISSIONS (
                hadm_id, subject_id, admittime, dischtime, deathtime,
                admission_type, admission_location, discharge_location,
                edregtime, edouttime, diagnosis, hospital_expire_flag,
                has_chartevents_data
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (hadm_id, subject_id, admittime, dischtime, deathtime,
              admission_type, admission_location, discharge_location,
              edregtime, edouttime, diagnosis, hospital_expire_flag,
              has_chartevents_data))

        conn.commit()
        st.success("New admission created successfully.")

        # Retrieve updated admissions data
        cursor.execute("SELECT * FROM ADMISSIONS")
        admissions = cursor.fetchall()
        df = pd.DataFrame(admissions, columns=["HADM ID", "Subject ID", "Admission Time", "Discharge Time",
                                               "Death Time", "Admission Type", "Admission Location",
                                               "Discharge Location", "ED Registration Time", "ED Out Time",
                                               "Diagnosis", "Hospital Expire Flag", "Has Chartevents Data"])
        st.subheader("Updated Admissions Data")
        st.dataframe(df)

if selected_option == "View Admissions":
    view_admissions()

if selected_option == "Create New Admission":
    create_admission()

home_button_end = st.button("🏠 Take me to Home Page", key = 'end')

if home_button_end:
    switch_page("Home")

