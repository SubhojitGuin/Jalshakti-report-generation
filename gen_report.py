from api_helper import get_data_from_sql , get_data_from_text
import pandas as pd
import pdfkit
import re
import random
# from template import html_template


# path_to_wkhtmltopdf = '/usr/bin/wkhtmltopdf'  # Default path in most Linux systems
# config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)


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
              <li>1. GroundWater Resource Assessment & Area Wise Categorization</li>
              <li>2. NOC Guidlines
                  <ul>
                      <li>2.1 Guidance on how to obtain NOC</li>
                      <li>2.2 Conditions for obtaining NOC for ground water extraction</li>
                  </ul>
              </li>
              <li>3. Training Opportunities</li>
              <li>4. Ground Water Management Practices</li>
              <li>5. Definition of GroundWater Terms</li>
             
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

def generate_report(State_name, Organisation_name, Date, update_status_callback):
    update_status_callback("Generating report...", 0)
    session_id = random.randint(0,1000)
    # GroundWater Resource Assessment
    update_status_callback("Fetching Ground Water Resource Assessment data...", 2)
    question_GRA = f"Give the Groundwater Resources data and classification of {State_name} and include only relevant columns"
    response_GRA = get_data_from_sql(question_GRA, session_id)
    response_GRA_html = re.sub(r'\n', '<br>', response_GRA)

    update_status_callback("Ground Water Resource Assessment Completed", 18)

    # NOC guidelines - Guidance on obtaining NOC
    update_status_callback("Fetching NOC guidelines...", 20)
    question_NOC1 = "Provide the Guidance on how to obtain NOC"
    response_NOC1 = get_data_from_text(question_NOC1, session_id)
    response_NOC_html1 = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', response_NOC1)
    response_NOC_html1 = re.sub(r'\n', '<br>', response_NOC_html1)

    update_status_callback("NOC Guidelines Completed", 32)

    # NOC guidelines - Conditions for obtaining NOC
    update_status_callback("Fetching conditions for obtaining NOC...", 35)
    question_NOC2 = "Provide the Conditions for obtaining NOC for ground water extraction"
    response_NOC2 = get_data_from_text(question_NOC2, session_id)
    response_NOC_html2 = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', response_NOC2)
    response_NOC_html2 = re.sub(r'\n', '<br>', response_NOC_html2)

    update_status_callback("NOC Conditions Completed", 45)
    
    # Training Opportunities
    update_status_callback("Fetching training opportunities...", 48)
    question_TO = "Provide the detailed training opportunities"
    response_TO = get_data_from_text(question_TO, session_id)
    response_TO_html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', response_TO)
    response_TO_html = re.sub(r'\n', '<br>', response_TO_html)

    update_status_callback("Training Opportunities Completed", 61)

    # Groundwater Management Practices
    update_status_callback("Fetching groundwater management practices...", 60)
    question_MP = "Provide the details of Ground Water Management Practices"
    response_MP = get_data_from_text(question_MP, session_id)
    response_MP_html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', response_MP)
    response_MP_html = re.sub(r'\n', '<br>', response_MP_html)

    update_status_callback("Groundwater Management Practices Completed", 73)

    # Ground Water Terms Definitions
    update_status_callback("Fetching glossary of groundwater terms...", 75)
    question_GT = "Provide the definitions of technical terms associated with groundwater"
    response_GT = get_data_from_text(question_GT, session_id)
    response_GT_html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', response_GT)
    response_GT_html = re.sub(r'\n', '<br>', response_GT_html)

    update_status_callback("Glossary of Groundwater Terms Completed", 88)

    # Generate final PDF report
    update_status_callback("Generating final PDF report...", 90)

    # response = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', response).replace("\n", "<br>")

    options = {"page-size": "A4"}
    # print(response)
    final_response = html_template.format(Organisation_name, Date ,response_GRA_html, response_NOC_html1, response_NOC_html2, response_TO_html, response_MP_html, response_GT_html)

    # pdf_output = pdfkit.from_string(final_response, False, options=options , configuration=config)
    pdf_output = pdfkit.from_string(final_response, False, options=options)

    update_status_callback("Report Generation Completed...", 100)

    return pdf_output