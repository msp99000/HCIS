import streamlit as st
import sqlite3
import pandas as pd
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
    menu_icon="cast", default_index=1, orientation="horizontal")
if selected == 'Home':
    switch_page('Home')
if selected == 'Admissions':
    switch_page('Admissions')
if selected == 'Dashboard':
    switch_page('Dashboard')

st.header('Patients')
menu_options = ["View Patients", "Register New Patient"]
selected_option = st.selectbox("Select Options", menu_options)

# Streamlit app functions
def view_patients():
    st.subheader("View Patients")
    cursor.execute("SELECT * FROM PATIENTS")
    patients = cursor.fetchall()
    df = pd.DataFrame(patients, columns=["Subject ID", "Language", "Religion", "Marital Status", "Ethnicity"])
    st.dataframe(df)

def register_patient():
    st.subheader("Register New Patient")
    subject_id = st.number_input("Subject ID", min_value=0, step=1)
    lang = st.text_input("Language")
    religion = st.text_input("Religion")
    marital_status = st.text_input("Marital Status")
    ethnicity = st.text_input("Ethnicity")

    if st.button("Save"):
        cursor.execute("INSERT INTO PATIENTS VALUES (?, ?, ?, ?, ?)",
                       (subject_id, lang, religion, marital_status, ethnicity))
        conn.commit()
        st.success("Patient registered successfully.")

if selected_option == 'View Patients':
    view_patients()

if selected_option == 'Register New Patient':
    register_patient()

home_button_end = st.button("🏠 Take me to Home Page", key = 'end')

if home_button_end:
    switch_page("Home")

