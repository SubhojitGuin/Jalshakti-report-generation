import streamlit as st

import pdfkit

import subprocess


def generate_pdf(text_input):

    question_input = st.text_area("You Want to Generate the GroundWater Report of which State?")

    if st.button("Generate Report"):

        options = {"page-size": "Letter"}

        pdf_output = pdfkit.from_string(text_input, False, options=options)

        st.download_button("Download Report", pdf_output, "Report.pdf", mime="application/pdf") 



if __name__ == "__main__":

    generate_pdf("Hey There")
    # Streamlit command with necessary arguments
    streamlit_cmd = [
        "streamlit", 
        "run", 
        "app.py",  # or use sys.argv[0] for the current file
        "--server.headless=true",  # Ensure it runs headless (good for servers)
        "--server.enableCORS=false",  # Disable CORS if needed for local testing
    ]

    # Run the Streamlit app using subprocess
    subprocess.run(streamlit_cmd)



    