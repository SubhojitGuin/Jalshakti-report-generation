from api_helper import get_data_from_sql , get_data_from_text
import pandas as pd
import pdfkit
import re
import markdown
# from template import html_template

html_template = """
  <html>
    <head>
      <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0 20px;
        }}
        h1, h2, h3 {{
            color: #2c3e50;
        }}
        h1 {{
            font-size: 28px;
            text-align: center;
        }}
        h2 {{
            font-size: 24px;
            margin-top: 40px;
        }}
        h3 {{
            font-size: 20px;
            margin-top: 20px;
        }}
        p {{
            font-size: 16px;
            margin: 10px 0;
        }}
        ul {{
            list-style-type: disc;
            margin-left: 40px;
        }}
        th {{
            background-color: #d3cac8c8;
        }}
        td, th {{
            width: 50px;
            text-align: left;
        }}
        table {{
            margin-top: -3600px;
            border-collapse: collapse;
            width: 100%;
            font-size: 12px;
        }}
        .cover-page, .page-break {{
            page-break-before: always;
        }}
        .cover-page {{
            text-align: center;
            padding-top: 200px;
        }}
        .cover-page p {{
            font-size: 18px;
        }}
        .table-of-contents {{
            margin: 20px 0;
            font-size: 20px;
        }}
        .table-of-contents ul {{
            list-style-type: none;
            padding-left: 0;
        }}
        .table-of-contents ul li {{
            padding: 5px 0;
        }}
        footer {{
            text-align: center;
            margin-top: 50px;
            font-size: 14px;
        }}
    </style>
    </head>
    <body>
      <!-- Cover Page -->
      <div class="cover-page">
          <h1>Comprehensive Guide on Ground Water Resource Management</h1>
          <h2>Groundwater Resource Assessment, Management, and Compliance</h2>
          <p>Prepared by: {}</p>
          <p>Date: {}</p>
      </div>

      <!-- Table of Contents -->
      <div class="page-break"></div>
      <h2>Table of Contents</h2>
      <div class="table-of-contents">
          <ul>
              <li>1. Introduction</li>
              <li>2. Ground Water Resource Assessment</li>
              <li>3. Categorization of Areas</li>
              <li>4. Ground Water Management Practices</li>
              <li>5. Conditions for Obtaining NOC for Ground Water Extraction</li>
              <li>6. Guidance on How to Obtain NOC</li>
              <li>7. Definition of Groundwater Terms</li>
              <li>8. Training Opportunities Related to Ground Water</li>
              <li>9. Conclusion</li>
              <li>10. References</li>
          </ul>
      </div>
      <div class="page-break"></div>
      <h1>Report</h1>
      <h2>GroundWater Resource Assessment & Area Wise Categorization</h2>
      {}
      <h2>NOC Guidelines</h2>
      <h3>Guidance on how to obtain NOC</h3>
      <p>{}</p>
      <h3>Conditions for obtaining NOC for ground water extraction</h3>
      <p>{}</p>
      <h2>Training Opportunities</h2>
      <p>{}</p>
      <h2>Ground Water Management Practices</h2>
      <p>{}</p>
      <h2>Definition of GroundWater Terms</h2>
      <p>{}</p>
    </body>
  </html>
  """

def generate_report(State_name, Organisation_name, Date):
  print("Generating report ...")

  with open("Report.txt", 'w') as report:
    report.write("Report\n")

  #-- GroundWater Resource Assessment --
  question_GRA = f"Give the Groundwater Resources data and classification of {State_name} and include only relevant columns"
  response_GRA = get_data_from_sql(question_GRA, "Streamlit")
  response_GRA_html = re.sub(r'\n', '<br>', response_GRA)

  with open("Report.txt", 'a') as report:
    report.write("\nGround Water Resource Assessment & Area Wise Categorization\n")
    report.write(repr(response_GRA))

  print("GroundWater Resource Assessment Completed")

  # -- NOC guidelines --
  question_NOC1 = "Provide the Guidance on how to obtain NOC"
  response_NOC1 = get_data_from_text(question_NOC1, "Streamlit")
  response_NOC_html1 = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', response_NOC1)
  response_NOC_html1 = re.sub(r'\n', '<br>', response_NOC_html1)

  with open("Report.txt", 'a') as report:
    report.write("\nNOC Guidelines\n")
    report.write("\nGuidance on how to obtain NOC\n")
    report.write(repr(response_NOC1))

  print("NOC Guidelines Completed")

  question_NOC2 = "Provide the Conditions for obtaining NOC for ground water extraction"
  response_NOC2 = get_data_from_text(question_NOC2, "Streamlit")
  response_NOC_html2 = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', response_NOC2)
  response_NOC_html2 = re.sub(r'\n', '<br>', response_NOC_html2)

  
  with open("Report.txt", 'a') as report:
    report.write("\nNOC Guidelines\n")
    report.write("\nConditions for obtaining NOC for ground water extraction\n")
    report.write(repr(response_NOC2))

  print("NOC Conditions Completed")
  
  # -- Training Oppurtunities --
  question_TO = "Provide the detailed training opportunities"
  response_TO = get_data_from_text(question_TO, "Streamlit")
  # response_TO_html = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', response_TO).replace("\n", "<br>")
  response_TO_html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', response_TO)
  response_TO_html = re.sub(r'\n', '<br>', response_TO_html)

  with open("Report.txt", 'a') as report:
    report.write("\nTraining Opportunities\n")
    report.write(repr(response_TO))

  print("Training Oppurtunities Completed")

  # -- Groundwater Management Practices --
  question_MP = "Provide the details of Ground Water Management Practices"
  response_MP = get_data_from_text(question_MP, "Streamlit")
  response_MP_html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', response_MP)
  response_MP_html = re.sub(r'\n', '<br>', response_MP_html)

  with open("Report.txt", 'a') as report:
    report.write("\nGround Water Management Practices\n")
    report.write(repr(response_MP))

  print("Groundwater Management Practices Completed")

  #-- Ground Water Terms Definitions --
  question_GT = "Provide the Glossary of technical terms used"
  response_GT = get_data_from_text(question_GT , "Streamlit")
  response_GT_html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', response_GT)
  response_GT_html = re.sub(r'\n', '<br>', response_GT_html)

  with open("Report.txt", 'a') as report:
    report.write("\nDefinition of GroundWater Terms\n")
    report.write(repr(response_GT))
  
  print("Ground Water Terms Definitions Completed")

  # response = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', response).replace("\n", "<br>")

  options = {"page-size": "A4"}
  # print(response)
  final_response = html_template.format(Organisation_name, Date ,response_GRA_html, response_NOC_html1, response_NOC_html2, response_TO_html, response_MP_html, response_GT_html)

  with open("Report.html", "w") as file:
    file.write(final_response)

  pdf_output = pdfkit.from_string(final_response, False, options=options)

  print("Report Generation Completed...")

  return pdf_output
  
# def generate_report(State_name):
#   question_NOC = "Provide the detailed guidelines for obtaining NOC"
#   response = get_data_from_text(question_NOC, "NOC")

#   response = markdown.markdown(response)
#   response = re.sub(r'\n+', '<br>', response)

#   options = {"page-size": "Letter"}

#   pdf_output = pdfkit.from_string(response, False, options=options)

#   return pdf_output