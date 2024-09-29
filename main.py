import streamlit as st
import time
from gen_report import generate_report
import datetime 
import logging

logging.basicConfig(level=logging.INFO)

st.title("Report Generator")
logging.info("***** App Started *****")

State_Name = st.text_input(label="You want to Generate a Report of Which State?")
Organisation_name = st.text_input("Your Organization Name:")
Date = st.date_input("Enter Date:", value=datetime.date.today())

# Validate user inputs
if st.button("Generate Report"):
    if not State_Name.strip():
        st.error("State Name cannot be empty!")
    elif not Organisation_name.strip():
        st.error("Organization Name cannot be empty!")
    else:
        with st.spinner("Generating the report..."):
            # Placeholder for status updates
            report_status = st.empty()  

        progress = st.progress(0)
        def update_status(message, progress_bar_value):
            progress.progress(progress_bar_value)  # Update progress bar dynamically
            report_status.write(message)  # Update status dynamically
            
        # Call to generate_report() and show download button
        response = generate_report(State_Name, Organisation_name, Date.strftime("%d/%m/%Y"), update_status)
        
        # Provide download button for the generated report
        st.success("Report Generation Completed!")
        st.download_button("Download Report", response, "Report.pdf", mime="application/pdf")
