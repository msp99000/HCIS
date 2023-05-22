
import streamlit as st
import pandas as pd
from styles import streamlit_style
from streamlit_extras.switch_page_button import switch_page
from streamlit_option_menu import option_menu
from texts import description

# Streamlit app and main function
def main():

    streamlit_style()

    # Horizontal Menu
    selected = option_menu(None, ["Home", "Patients", "Admissions", 'Dashboard'], 
        icons=['house', 'cloud-upload', "list-task", 'gear'], 
        menu_icon="cast", default_index=0, orientation="horizontal")
    if selected == 'Patients':
        switch_page('Patients')
    if selected == 'Admissions':
        switch_page('Admissions')
    if selected == 'Dashboard':
        switch_page('Dashboard')

    # App Logo
    st.image('logo.png')

    # Add header
    st.title('HCIS - Healthcare Information Systems')

    st.write(description)
    st.header(' ')

if __name__ == '__main__':
    main()
