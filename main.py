import streamlit as st
import subprocess
import time
from gen_report import generate_report

st.title("Report Generator")
print("\n\n***** App Started *****\n\n")

State_Name = st.text_input(label="You want to Generate a Report of Which State?")

if st.button("Generate Report"):
    noc_response = generate_report(State_Name)
    # print(noc_response)
    st.download_button("Download Report", noc_response, "Report.pdf", mime="application/pdf")

# def generate_pdf(text_input):

#     question_input = st.text_area("You Want to Generate the GroundWater Report of which State?")

#     if st.button("Generate Report"):

        

         



# if __name__ == "__main__":

#     generate_pdf("Hey There")
#     # Streamlit command with necessary arguments
#     streamlit_cmd = [
#         "streamlit", 
#         "run", 
#         "app.py",  # or use sys.argv[0] for the current file
#         "--server.headless=true",  # Ensure it runs headless (good for servers)
#         "--server.enableCORS=false",  # Disable CORS if needed for local testing
#     ]

#     # Run the Streamlit app using subprocess
#     subprocess.run(streamlit_cmd)



    